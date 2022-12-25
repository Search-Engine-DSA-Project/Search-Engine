import json

import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.snowball import SnowballStemmer
import pandas as pd
import re

punctuations = re.compile(r'[^\w\s]')
stop_words = set(stopwords.words('english'))
tokenizer = WordPunctTokenizer()
stemmer = SnowballStemmer('english')


def temp_parse(x):
    x = tokenizer.tokenize(punctuations.sub('', x))
    x = [stemmer.stem(word) for word in x if word.lower() not in stop_words]
    return x


def json_parser(path1):
    with open(path1, 'r') as f:
        df = pd.DataFrame(json.load(f))
    df['content'] = df['content'].apply(temp_parse)
    unique_tokens = np.unique(token for doc in df['content'].values for token in doc)
    doc_dict = {row['id']: row['content'] for row in df.to_dict(orient='records')}
    return unique_tokens, doc_dict
