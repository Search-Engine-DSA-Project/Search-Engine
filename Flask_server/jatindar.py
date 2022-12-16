import nltk
import re
import os
import json
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

tokenizer = nltk.RegexpTokenizer(r"\w+")
ps = PorterStemmer()
final_data = []
stopwords = stopwords.words('english')
for temp in os.listdir(".\\Dataset\\temp_testing\\"):
    text = open(f'.\\Dataset\\temp_testing\\{temp}', "r").read()
    data__ = json.loads(text)
    __data__ = []
    for data in data__:
        data["content"] = tokenizer.tokenize(data["content"])
        data["content"] = [ps.stem(word) for word in data["content"]]
        data["content"] = [word for word in data["content"] if word not in stopwords]
        for word in range(len(data["content"])):
            x = {data["content"][word]: word}
            __data__.append(x)
        final_data.append({data["id"]: __data__})