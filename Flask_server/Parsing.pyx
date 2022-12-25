# Cython files are compiled to C files not to be looked at now, are under testing


# def json_parser(path):
#     def temp_parse(x):
#         x = punctuations.tokenize(x)
#         x = [PorterStemmer().stem(word) for word in x if word.lower() not in stop_words]
#         return x
#     open_file = open(path, 'r')
#     file_data = open_file.read()
#     df = pds.DataFrame(json.loads(file_data))
#     df['content'] = df['content'].apply(temp_parse)
#     return [np.unique(np.concatenate(df['content'].values)), df.set_index('id')['content'].to_dict()]
import json
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
        x = tokenizer.tokenize(punctuations.sub('', x))
        x = [stemmer.stem(word) for word in x if word.lower() not in stop_words]
        return x

    with open(path1, 'r') as f:
        df = pd.DataFrame(json.load(f))
    df['content'] = df['content'].apply(temp_parse)
    unique_tokens = set(token for doc in df['content'].values for token in doc)
    doc_dict = {row['id']: row['content'] for row in df.to_dict(orient='records')}
    return unique_tokens, doc_dict
