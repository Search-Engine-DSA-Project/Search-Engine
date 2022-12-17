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
