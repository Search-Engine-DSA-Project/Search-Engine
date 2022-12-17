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
import numpy as np
import pandas as pds
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

punctuations = RegexpTokenizer(r'\w+')
stop_words = stopwords.words('english')


def json_parser(path):
    def temp_parse(x):
        x = punctuations.tokenize(x)
        x = [PorterStemmer().stem(word) for word in x if word.lower() not in stop_words]
        return x

    open_file = open(path, 'r')
    file_data = open_file.read()
    df = pds.DataFrame(json.loads(file_data))

    df['content'] = df['content'].apply(temp_parse)

    return [np.unique(np.concatenate(df['content'].values)), df.set_index('id')['content'].to_dict()]
