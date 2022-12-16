# TODO: Creating Parser
#   1. Create a function for parsing the JSON files
#   2. Parsing details:
#       a. Remove all the punctuations (Done)
#       b. Remove all the URLs (turn out data doesn't have any URLs so step skipped)
#       c. Remove all the redundant words (Done)
#       d. Remove all the stop words (Done)
#       e. Stem the words (Done)
#       f. Creating a list of words and calling em' tokens (Done)
#       g. Return the tokens (Done)

import json
import pandas as pds
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
import itertools


def json_parser(path, flag=False): # Flag false returns lexicon else Forward Index
    punctuations = RegexpTokenizer(r'\w+')
    open_file = open(path, 'r')
    file_data = open_file.read()
    df = pds.DataFrame(json.loads(file_data))
    open_file.close()

    def temp_parse(x):
        stop_words = stopwords.words('english')
        x = punctuations.tokenize(x)
        x = [PorterStemmer().stem(i) for i in x]
        x = [word for word in x if word not in stop_words]
        return x

    df["content"] = df["content"].apply(temp_parse)
    if flag:
        # print(df.set_index("id")[["content"]])
        return df.set_index('id')['content'].to_dict()
    return list(set(itertools.chain.from_iterable(df["content"].tolist())))
