# -*- coding: utf-8 -*-
# @Author: Shuang0420
# @Date:   2018-08-06 19:21:37
# @Last Modified by:   Shuang0420
# @Last Modified time: 2018-08-06 19:21:37
import os
import sys    
reload(sys)   
sys.setdefaultencoding('utf8')
import os
import sys
from StanfordNLP import StanfordNLP
import json


def parse(text):
    text = str(text)
    print(text)
    segments = StanfordNLP.segment(text)
    segmented_text = [text[start: end] for start, end in zip(segments[:-1], segments[1:])]
    # print segmented_text
    
    pos_tags = StanfordNLP.pos_tag(text)
    segmented_pos, segmented_ner = [], []

    named_entities = StanfordNLP.ner(text)
    for pos_tag in pos_tags:
        segmented_pos.append(pos_tag.name)
        ner = u"Other"
        for named_entity in named_entities:
            if pos_tag.start >= named_entity.start and pos_tag.start <= named_entity.end and pos_tag.end <= named_entity.end:
                ner = named_entity.name
                break
        segmented_ner.append(ner)

    return segmented_text, segmented_pos, segmented_ner

def main():
    StanfordNLP.start_service()

    text = "慈禧命醇亲王奕𫍽在此处开始营造仪銮殿"

    text1 = "慈禧命醇亲王奕"

    text2 = "𫍽在此处开始营造仪銮殿"

    segmented_answer, answer_pos, answer_ner = parse(text1)
    print("{}\n{}\n{}\n".format(segmented_answer, answer_pos, answer_ner))

    segmented_answer, answer_pos, answer_ner = parse(text2)
    print("{}\n{}\n{}\n".format(segmented_answer, answer_pos, answer_ner))

    segmented_answer, answer_pos, answer_ner = parse(text)
    print("{}\n{}\n{}\n".format(segmented_answer, answer_pos, answer_ner))
    # with open(filename,"r") as fin:
    #     data = json.load(fin)
    #     data_ = []
    #     for cc in data:
    #         text = cc["context_text"]
    #         segmented_context,context_pos, context_ner = parse(text)

    #         qas_ = []
    #         for q in cc["qas"]:
    #             answers = q["answers"]
    #             segmented_answers, answers_pos, answers_ner = [], [], []
    #             for ans in answers:
    #                 segmented_answer, answer_pos, answer_ner = parse(ans)
    #                 segmented_answers.append(segmented_answer)
    #                 answers_pos.append(answer_pos)
    #                 answers_ner.append(answer_ner)
    #             query_text = q["query_text"]
    #             segmented_question, question_pos, question_ner = parse(query_text)
    #             qas_.append({
    #                 "query_text": query_text,
    #                 "query_id": q["query_id"],
    #                 "segmented_question": segmented_question,
    #                 "question_pos": question_pos,
    #                 "question_ner": question_ner,
    #                 "answers": answers,
    #                 "segmented_answers": segmented_answers,
    #                 "answers_pos": answers_pos,
    #                 "answers_ner": answers_ner,
    #                 "answer_spans": q["answer_spans"]
    #             })



    #         cc_ = {"context_id": cc["context_id"], 
    #                 "context_text": text,
    #                 "segmented_context": segmented_context,
    #                 "context_pos": context_pos,
    #                 "context_ner": context_ner,
    #                 "qas": qas_
    #                 }
    #         data_.append(cc_)
    #         # break

    # with open("data2/" + filename.split("/")[-1], "w") as fw:
    #     json.dump(data_, fw, ensure_ascii=False)


if __name__ == "__main__":
    filename = sys.argv[1]
    main()