from concurrent.futures import ProcessPoolExecutor
import math
import json
import os
import datetime
import itertools
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.snowball import SnowballStemmer
import pandas as pd
import re
from collections import OrderedDict

punctuations = re.compile(r'[^\w\s]')
stop_words = set(stopwords.words('english'))
tokenizer = WordPunctTokenizer()
stemmer = SnowballStemmer('english')
temp = 0


def temp_parse(x):
    x = tokenizer.tokenize(punctuations.sub('', x))
    x = [stemmer.stem(word) for word in x if word.lower() not in stop_words]
    return x


def conversion(x):
    temp = {}
    temp_var = 0
    try:
        temp_var = 1 / (len(x) + 1)
    except Exception as e:
        pass
    for i in range(len(x)):
        if x[i] not in temp:
            temp[x[i]] = temp_var
        else:
            temp[x[i]] += temp_var
    return temp


def json_parser(path1):
    with open(path1, 'r') as f:
        df = pd.DataFrame(json.load(f))
    df['content'] = df['content'].apply(temp_parse)
    unique_tokens = list(set(itertools.chain.from_iterable(df["content"].tolist())))
    df["content"] = df["content"].apply(conversion)
    doc_dict = {row['url']: row['content'] for row in df.to_dict(orient='records')}
    return unique_tokens, doc_dict


def inverted_index(path2):
    unique_tokens, doc_dict = json_parser(path2)
    inverted_indexing = {}
    for unique_token in unique_tokens:
        inverted_indexing[unique_token] = {}
    for doc_id, tokens in doc_dict.items():
        for word, pos_list in tokens.items():
            inverted_indexing[word][doc_id] = pos_list
    return inverted_indexing
