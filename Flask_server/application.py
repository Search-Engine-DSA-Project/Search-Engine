# cython: language_level=3
from collections import defaultdict, Counter
# from concurrent.futures import ProcessPoolExecutor
import json
import os
import datetime
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.snowball import SnowballStemmer
import pandas as pd
import re

punctuations = re.compile(r'[^\w\s]')
stop_words = set(stopwords.words('english'))
tokenizer = WordPunctTokenizer()
stemmer = SnowballStemmer('english')


def json_parser(path1):
    def temp_parse(x):
        # Tokenize and stem the input string
        x = tokenizer.tokenize(punctuations.sub('', x))
        x = [stemmer.stem(word) for word in x if word.lower() not in stop_words]
        return x

    with open(path1, 'r') as f:
        df = pd.DataFrame(json.load(f))
    df['content'] = df['content'].apply(temp_parse)
    unique_tokens = set(token for doc in df['content'].values for token in doc)
    doc_dict = {row['id']: row['content'] for row in df.to_dict(orient='records')}
    return unique_tokens, doc_dict


# def create_inverted_index(path3):
#     with ProcessPoolExecutor() as executor:
#         indexes = list(executor.map(inverted_index, (path3 + x for x in os.listdir(path3))))
#     merged_index = defaultdict(Counter)
#     for index in indexes:
#         for token, doc_counts in index.items():
#             merged_index[token] += doc_counts
#     return merged_index
def inverted_index(path2):
    unique_tokens, doc_dict = json_parser(path2)
    inverted_indexing = {}
    for doc_id, tokens in doc_dict.items():
        for token in tokens:
            if token not in inverted_indexing:
                inverted_indexing[token] = {}
            if doc_id in inverted_indexing[token]:
                inverted_indexing[token][doc_id] += 1
            else:
                inverted_indexing[token][doc_id] = 1
    return inverted_indexing


def create_inverted_index(path):
    merged_index = defaultdict(Counter)
    for file in os.listdir(path):
        index = inverted_index(path + file)
        for token, doc_counts in index.items():
            merged_index[token] += doc_counts
    return merged_index


if __name__ == '__main__':
    path = ".\\temp_testing\\"
    x1 = datetime.datetime.now()
    index = create_inverted_index(path)
    with open('.\\output_test.json', 'w', encoding='utf-8') as fx:
        json.dump(index, fx)
    print(f"Time taken: {datetime.datetime.now() - x1}")
