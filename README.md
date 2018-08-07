# CoreNLP-Chinese-Tool
Stanford CoreNLP for Chinese language

# Install
```
wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-01-31.zip
wget http://nlp.stanford.edu/software/stanford-chinese-corenlp-2018-02-27-models.jar

unzip stanford-corenlp-full-2018-01-31.zip
mv stanford-chinese-corenlp-2018-02-27-models.jar stanford-corenlp-full-2018-01-31/
```

# Comments
High precision but not robust enough.

For example, ``text1`` and ``text2`` runs correctly but ``text`` crashes the system including the corenlp.run server.
```
text = "慈禧命醇亲王奕𫍽在此处开始营造仪銮殿"

text1 = "慈禧命醇亲王奕"

text2 = "𫍽在此处开始营造仪銮殿"
```

Results:
```
慈禧命醇亲王奕
<Response [200]>
{"tokens":[{"index":-1,"word":"慈禧","originalText":"慈禧","characterOffsetBegin":0,"characterOffsetEnd":2},{"index":-1,"word":"命醇","originalText":"命醇","characterOffsetBegin":2,"characterOffsetEnd":4},{"index":-1,"word":"亲王奕","originalText":"亲王奕","characterOffsetBegin":4,"characterOffsetEnd":7}]}
<Response [200]>
{"sentences":[{"index":0,"tokens":[{"index":1,"word":"慈禧","originalText":"慈禧","characterOffsetBegin":0,"characterOffsetEnd":2,"pos":"NN"},{"index":2,"word":"命醇","originalText":"命醇","characterOffsetBegin":2,"characterOffsetEnd":4,"pos":"NN"},{"index":3,"word":"亲王奕","originalText":"亲王奕","characterOffsetBegin":4,"characterOffsetEnd":7,"pos":"NN"}]}]}
<Response [200]>
{"sentences":[{"index":0,"entitymentions":[],"tokens":[{"index":1,"word":"慈禧","originalText":"慈禧","lemma":"慈禧","characterOffsetBegin":0,"characterOffsetEnd":2,"pos":"NN","ner":"O"},{"index":2,"word":"命醇","originalText":"命醇","lemma":"命醇","characterOffsetBegin":2,"characterOffsetEnd":4,"pos":"NN","ner":"O"},{"index":3,"word":"亲王奕","originalText":"亲王奕","lemma":"亲王奕","characterOffsetBegin":4,"characterOffsetEnd":7,"pos":"NN","ner":"O"}]}]}
['\xe6\x85', '\x88\xe7', '\xa6\xa7\xe5']
[u'NN', u'NN', u'NN']
[u'Other', u'Other', u'Other']

𫍽在此处开始营造仪銮殿
<Response [200]>
{"tokens":[{"index":-1,"word":"𫍽","originalText":"𫍽","characterOffsetBegin":0,"characterOffsetEnd":2},{"index":-1,"word":"在此处","originalText":"在此处","characterOffsetBegin":2,"characterOffsetEnd":5},{"index":-1,"word":"开始","originalText":"开始","characterOffsetBegin":5,"characterOffsetEnd":7},{"index":-1,"word":"营造","originalText":"营造","characterOffsetBegin":7,"characterOffsetEnd":9},{"index":-1,"word":"仪銮殿","originalText":"仪銮殿","characterOffsetBegin":9,"characterOffsetEnd":12}]}
<Response [200]>
{"sentences":[{"index":0,"tokens":[{"index":1,"word":"𫍽","originalText":"𫍽","characterOffsetBegin":0,"characterOffsetEnd":2,"pos":"NN"},{"index":2,"word":"在此处","originalText":"在此处","characterOffsetBegin":2,"characterOffsetEnd":5,"pos":"AD"},{"index":3,"word":"开始","originalText":"开始","characterOffsetBegin":5,"characterOffsetEnd":7,"pos":"VV"},{"index":4,"word":"营造","originalText":"营造","characterOffsetBegin":7,"characterOffsetEnd":9,"pos":"VV"},{"index":5,"word":"仪銮殿","originalText":"仪銮殿","characterOffsetBegin":9,"characterOffsetEnd":12,"pos":"NN"}]}]}
<Response [200]>
{"sentences":[{"index":0,"entitymentions":[{"docTokenBegin":0,"docTokenEnd":2,"tokenBegin":0,"tokenEnd":2,"text":"𫍽在此处","characterOffsetBegin":0,"characterOffsetEnd":5,"ner":"ORGANIZATION"}],"tokens":[{"index":1,"word":"𫍽","originalText":"𫍽","lemma":"𫍽","characterOffsetBegin":0,"characterOffsetEnd":2,"pos":"NN","ner":"ORGANIZATION"},{"index":2,"word":"在此处","originalText":"在此处","lemma":"在此处","characterOffsetBegin":2,"characterOffsetEnd":5,"pos":"AD","ner":"ORGANIZATION"},{"index":3,"word":"开始","originalText":"开始","lemma":"开始","characterOffsetBegin":5,"characterOffsetEnd":7,"pos":"VV","ner":"O"},{"index":4,"word":"营造","originalText":"营造","lemma":"营造","characterOffsetBegin":7,"characterOffsetEnd":9,"pos":"VV","ner":"O"},{"index":5,"word":"仪銮殿","originalText":"仪銮殿","lemma":"仪銮殿","characterOffsetBegin":9,"characterOffsetEnd":12,"pos":"NN","ner":"O"}]}]}
['\xf0\xab', '\x8d\xbd\xe5', '\x9c\xa8', '\xe6\xad', '\xa4\xe5\xa4']
[u'NN', u'AD', u'VV', u'VV', u'NN']
[u'ORGANIZATION', u'ORGANIZATION', u'Other', u'Other', u'Other']

慈禧命醇亲王奕𫍽在此处开始营造仪銮殿
<Response [500]>
java.util.concurrent.ExecutionException: java.lang.IndexOutOfBoundsException: Index: 18, Size: 18
Traceback (most recent call last):
  File "test.py", line 104, in <module>
    main()
  File "test.py", line 53, in main
    segmented_answer, answer_pos, answer_ner = parse(text)
  File "test.py", line 19, in parse
    segments = StanfordNLP.segment(text)
  File "/Users/xushuang/zhuiyi/CoreNLP-Chinese-Tool/StanfordNLP/StanfordNLP.py", line 52, in segment
    matches = StanfordNLP._make_request("tokenize", text)
  File "/Users/xushuang/zhuiyi/CoreNLP-Chinese-Tool/StanfordNLP/StanfordNLP.py", line 120, in _make_request
    return json.loads(response.content)
  File "/Users/xushuang/anaconda/envs/python2.7/lib/python2.7/json/__init__.py", line 339, in loads
    return _default_decoder.decode(s)
  File "/Users/xushuang/anaconda/envs/python2.7/lib/python2.7/json/decoder.py", line 364, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/Users/xushuang/anaconda/envs/python2.7/lib/python2.7/json/decoder.py", line 382, in raw_decode
    raise ValueError("No JSON object could be decoded")
ValueError: No JSON object could be decoded
```


