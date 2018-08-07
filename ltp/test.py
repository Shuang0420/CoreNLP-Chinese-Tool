# -*- coding: utf-8 -*-
# @Author: Shuang0420
# @Date:   2018-08-07 15:21:37
# @Last Modified by:   Shuang0420
# @Last Modified time: 2018-08-07 15:21:37
import os
import sys    
reload(sys)   
sys.setdefaultencoding('utf8')
import json


LTP_DATA_DIR = '/root/ltp/ltp_data_v3.4.0/'
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')

from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
segmentor = Segmentor()  
segmentor.load(cws_model_path)  

postagger = Postagger() 
postagger.load(pos_model_path)  

recognizer = NamedEntityRecognizer() 
recognizer.load(ner_model_path)  



def parse(text):
    text = str(text)
    print(text)
    segmented_text = segmentor.segment(text)
   
    segmented_pos = postagger.postag(segmented_text)

    segmented_ner = recognizer.recognize(segmented_text, segmented_pos)

    segmented_ner = [ner.split("-")[-1] for ner in segmented_ner]

    return list(segmented_text), list(segmented_pos), list(segmented_ner)

def main():
    text = """在第二部独孤剑做为配角中更是被玩家评价为武功极其高强，不仅传给南宫飞云全身武功，而且自创改良天魔解体大法神功。"""
    segmented_context,context_pos, context_ner = parse(text)
    print segmented_context,context_pos, context_ner

if __name__ == "__main__":
    main()
