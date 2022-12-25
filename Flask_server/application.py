from collections import defaultdict, Counter
from concurrent.futures import ProcessPoolExecutor
import json
import os
import datetime
from time import time
import numpy as np
import itertools
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.snowball import SnowballStemmer
import pandas as pd
import re

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
    for i in range(len(x)):
        if x[i] not in temp:
            temp[x[i]] = [i]
        else:
            temp[x[i]].append(i)
    return temp


def json_parser(path1):
    with open(path1, 'r') as f:
        df = pd.DataFrame(json.load(f))
    df['content'] = df['content'].apply(temp_parse)
    unique_tokens = list(set(itertools.chain.from_iterable(df["content"].tolist())))
    df["content"] = df["content"].apply(conversion)
    doc_dict = {row['id']: row['content'] for row in df.to_dict(orient='records')}
    return unique_tokens, doc_dict


def inverted_index(path2):
    unique_tokens, doc_dict = json_parser(path2)
    global temp
    temp += len(doc_dict)
    print(temp)
    inverted_indexing = {}
    for unique_token in unique_tokens:
        inverted_indexing[unique_token] = {}
    for doc_id, tokens in doc_dict.items():
        for word, pos_list in tokens.items():
            inverted_indexing[word][doc_id] = pos_list
    return inverted_indexing


def create_inverted_index(path3):
    with ProcessPoolExecutor() as executor:
        indexes = list(executor.map(inverted_index, (path3 + x for x in os.listdir(path3))))
    merged_index = {}
    for inv_index in indexes:
        for token, docs_ in inv_index.items():
            if token not in merged_index:
                merged_index[token] = {}
            merged_index[token].update(docs_)
    return merged_index


def dynamic_content_addition(index_addition, merged_index):
    indexes = [index_addition, merged_index]
    merged_index = {}
    for inv_index in indexes:
        for token, docs_ in inv_index.items():
            if token not in merged_index:
                merged_index[token] = {}
            merged_index[token].update(docs_)
    return merged_index


def page_rank():
    pass


def single_word_search():
    open_file = open("output_test1.json", 'r')
    file_data = open_file.read()
    file1_data = json.loads(file_data)
    data = input("Enter Here: ")
    start = time()
    hassan = file1_data[data]
    print(hassan)
    print(time() - start)


def multi_word_search():
    open_file = open("output_test1.json", 'r')
    file_data = open_file.read()
    file1_data = json.loads(file_data)
    data = input("Enter Here: ")
    data = temp_parse(data)
    [print(file1_data[x]) for x in data]
    pass


# def create_inverted_index():
#     # dataset = os.listdir(path)
#     # with multiprocessing.Pool(processes=6) as p:
#     #     __inverted_list__ = p.map(inverted_index, [(path + x) for x in dataset])
#     # return __inverted_list__
#     dataset = os.listdir(path)
#     __inverted_list__ = []
#     for x in dataset:
#         __inverted_list__.append(inverted_index(path + x))
#     return __inverted_list__
#
#
# def merge_dict(merge_list):
#     merged_dict = {}
#     for item in merge_list:
#         for outer_key, outer_value in item.items():
#             if outer_key not in merged_dict:
#                 merged_dict[outer_key] = outer_value
#                 continue
#             for inner_key, inner_value in outer_value.items():
#                 if inner_key not in merged_dict[outer_key]:
#                     merged_dict[outer_key][inner_key] = inner_value
#                     continue
#                 merged_dict[outer_key][inner_key] += inner_value
#     return merged_dict


# def inverted_index(path):
#     lexicon = create_lexicon(path)
#     forward_indexing = forward_index(path)
#     inverted_indexing = {i: [] for i in lexicon}
#     for doc_id, tokens in forward_indexing.items():
#         for token in tokens:
#             if doc_id not in inverted_indexing[token]:
#                 inverted_indexing[token].append(doc_id)
#     return inverted_indexing
# def create_inverted_index(path):
#     merged_index = defaultdict(Counter)
#     for file in os.listdir(path):
#         index = inverted_index(path + file)
#         for token, doc_counts in index.items():
#             merged_index[token] += doc_counts
#     return merged_index


if __name__ == '__main__':
    path = ".\\temp_testing\\"
    x1 = datetime.datetime.now()
    index = create_inverted_index(path)
    with open('.\\output_test1.json', 'w', encoding='utf-8') as fx:
        json.dump(index, fx)
    print(temp)
    print(f"Time taken: {datetime.datetime.now() - x1}")

# if __name__ == '__main__':
#     # path = "X:\\Dataset\\nela-gt-2021\\newsdata\\"
#     path = ".\\temp_testing\\"
#     x1 = datetime.datetime.now()
#     # index = create_inverted_index(path)
#     temp = 0
#     for file in os.listdir(path):
#         file1 = open(path + file, "r")
#         file_data = json.loads(file1.read())
#         file1.close()
#         temp += len(file_data)
#         print(temp)
#     print(temp)
#     print(f"Time taken: {datetime.datetime.now() - x1}")
