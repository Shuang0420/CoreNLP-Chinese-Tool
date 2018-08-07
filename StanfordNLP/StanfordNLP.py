# -*- coding: utf-8 -*-
import os
import sys
import json
import socket
import requests
import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir)
from Language.NamedEntity import NamedEntity
from Language.PosTag import PosTag
from Language.DPTreePath import DPTreePath


__metaclass__ = type


class StanfordNLP:
    _HostAddress = "127.0.0.1"
    _HostPort = 9000
    _URL = "http://" + _HostAddress + ":" + str(_HostPort)
    _Timeout = 15000
    _StanfordNLPPath = "~/stanford-corenlp-python/stanford-corenlp-full-2018-01-31/"
    _ServerClass = "edu.stanford.nlp.pipeline.StanfordCoreNLPServer"
    _ServerProperties = "StanfordCoreNLP-chinese.properties"

    @staticmethod
    def start_service():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection = sock.connect_ex((StanfordNLP._HostAddress, StanfordNLP._HostPort))
        if connection == 0:
            print("Service is already started.")
            return False
        os.system(" ".join(["start_stanford_nlp_server ",
                            StanfordNLP._StanfordNLPPath, StanfordNLP._ServerClass, StanfordNLP._ServerProperties,
                            str(StanfordNLP._HostPort), str(StanfordNLP._Timeout)]))
        while connection != 0:
            connection = sock.connect_ex((StanfordNLP._HostAddress, StanfordNLP._HostPort))
        return True

    @staticmethod
    def stop_service():
        with open("/tmp/corenlp.shutdown", "r") as key_file:
            key = key_file.read()
        command = "curl http://" + StanfordNLP._HostAddress + ":" + str(StanfordNLP._HostPort) + "/shutdown?key=" + key
        os.system(command)

    @staticmethod
    def segment(text):
        if len(text) == 0:
            return []
        matches = StanfordNLP._make_request("tokenize", text)
        segment_set = set()
        for match in matches[u"tokens"]:
            segment_set.add(match[u"characterOffsetBegin"])
            segment_set.add(match[u"characterOffsetEnd"])
        ret = list(segment_set)
        ret.sort()
        return ret

    @staticmethod
    def pos_tag(text):
        if len(text) == 0:
            return []
        matches = StanfordNLP._make_request("pos", text)
        ret = []
        for sentences in matches[u"sentences"]:
            for match in sentences[u"tokens"]:
                ret.append(PosTag(match[u"characterOffsetBegin"], match[u"characterOffsetEnd"],
                                  match[u"pos"]))
        return ret

    @staticmethod
    def ner(text):
        if len(text) == 0:
            return []
        matches = StanfordNLP._make_request("ner", text)
        ret = []
        for sentences in matches[u"sentences"]:
            for match in sentences[u"entitymentions"]:
                ret.append(NamedEntity(match[u"characterOffsetBegin"], match[u"characterOffsetEnd"],
                                       match[u"ner"]))
        return ret

    @staticmethod
    def dp_tree_path(text):
        if len(text) == 0:
            return []
        matches = StanfordNLP._make_request("depparse", text)
        ret = []
        root = {u"characterOffsetBegin": sys.maxint, u"characterOffsetEnd": sys.maxint}
        for sentences in matches[u"sentences"]:
            tokens = sentences[u"tokens"]
            for match in sentences[u"enhancedPlusPlusDependencies"]:
                dependent_token = tokens[match[u"dependent"] - 1] if match[u"dependent"] > 0 else root
                dep_start = dependent_token[u"characterOffsetBegin"]
                dep_end = dependent_token[u"characterOffsetEnd"]

                governor_token = tokens[match[u"governor"] - 1] if match[u"governor"] > 0 else root
                gov_start = governor_token[u"characterOffsetBegin"]
                gov_end = governor_token[u"characterOffsetEnd"]

                if dep_end <= gov_start:
                    ret.append(DPTreePath(dep_start, dep_end, gov_start, gov_end, u"DP_UP " + match[u"dep"]))
                elif dep_start >= gov_end:
                    ret.append(DPTreePath(gov_start, gov_end, dep_start, dep_end, u"DP_DOWN " + match[u"dep"]))
                else:
                    raise ValueError("Intertwined tokens")
        return ret

    @staticmethod
    def _make_request(annotator, text):
        properties = {
            "annotators": annotator,
            "outputFormat": "json"
        }
        response = requests.post(StanfordNLP._URL + "/?properties=" + json.dumps(properties), data=text.encode("utf-8"))
        print(response)
        print(response.content)
        return json.loads(response.content)


def main():
    StanfordNLP.start_service()
    text = u"关于公司发行股份购买资产事宜公司因收购徐文辉等共6名股东持有的上海泰欣环境工程股份有限公司（以下简称“泰欣环境”）、" \
           u"凌亮等持有的浙江汉蓝环境科技有限公司（以下简称“汉蓝环境”）相关资产及业务，构成发行股份购买资产。经公司申请，公司股票自" \
           u"2018年3月20日起连续停牌。2018年3月24日，根据相关规定公司披露了《关于发行股份购买资产停牌前股东情况的公告》；2018年4月20日，" \
           u"由于本次发行股份购买资产涉及事项较多，各中介机构相关工作尚未最终完成，经公司申请，公司股票自2018年4月20日起继续停牌；" \
           u"以上相关信息详见2018年3月20日、3月24日、4月20日公司指定信息披露报刊和上海证券交易所网站。" \
           u"（编号临2018-019、临2018-021、临2018-035）目前，公司正在有序推动本次发行股份购买资产的各项工作，停牌期间，" \
           u"公司将根据本次发行股份购买资产的进展情况，严格按照相关法律法规的要求及时履行信息披露义务。"
    segments = StanfordNLP.segment(text)
    for start, end in zip(segments[:-1], segments[1:]):
        print(text[start: end])

    named_entities = StanfordNLP.ner(text)
    for named_entity in named_entities:
        print(text[named_entity.start: named_entity.end] + " : " + named_entity.name)

    pos_tags = StanfordNLP.pos_tag(text)
    for pos_tag in pos_tags:
        print(text[pos_tag.start: pos_tag.end] + " : " + pos_tag.name)

    dp_tree_paths = StanfordNLP.dp_tree_path(text)
    for dp_tree_path in dp_tree_paths:
        print(text[dp_tree_path.first_start: dp_tree_path.first_end] + " --" + dp_tree_path.name + "--> " +
              text[dp_tree_path.second_start: dp_tree_path.second_end])

    StanfordNLP.stop_service()


if __name__ == "__main__":
    main()
