import datetime
import os
from Inverted_Indexing import inverted_index

########################################################################################################################

# punctuations = RegexpTokenizer(r'\w+')
# stop_words = stopwords.words('english')
#
#
# def json_parser(path):
#     def temp_parse(x):
#         x = punctuations.tokenize(x)
#         x = [PorterStemmer().stem(word) for word in x if word.lower() not in stop_words]
#         return x
#
#     open_file = open(path, 'r')
#     file_data = open_file.read()
#     df = pds.DataFrame(json.loads(file_data))
#
#     df['content'] = df['content'].apply(temp_parse)
#
#     return [df.set_index('id')['content'].to_dict(), np.unique(np.concatenate(df['content'].values))]
#
#
# def inverted_index(path):
#     lexicon_forward_index = json_parser(path)
#     inverted_indexing = {i: {} for i in lexicon_forward_index[1]}
#     for doc_id, tokens in lexicon_forward_index[0].items():
#         for token in tokens:
#             if doc_id in inverted_indexing[token]:
#                 inverted_indexing[token][doc_id] += 1
#                 continue
#             inverted_indexing[token][doc_id] = 1
#     return inverted_indexing
#

########################################################################################################################


def create_inverted_index():
    # dataset = os.listdir(path)
    # with multiprocessing.Pool(processes=6) as p:
    #     __inverted_list__ = p.map(inverted_index, [(path + x) for x in dataset])
    # return __inverted_list__
    dataset = os.listdir(path)
    __inverted_list__ = []
    for x in dataset:
        __inverted_list__.append(inverted_index(path + x))
    return __inverted_list__


def merge_dict(merge_list):
    merged_dict = {}
    for item in merge_list:
        for outer_key, outer_value in item.items():
            if outer_key not in merged_dict:
                merged_dict[outer_key] = outer_value
                continue
            for inner_key, inner_value in outer_value.items():
                if inner_key not in merged_dict[outer_key]:
                    merged_dict[outer_key][inner_key] = inner_value
                    continue
                merged_dict[outer_key][inner_key] += inner_value
    return merged_dict


if __name__ == '__main__':
    # 'X:\\Dataset\\nela-gt-2021\\newsdata\\'
    path = ".\\temp_testing\\"
    x1 = datetime.datetime.now()
    open('.\\output_test.json', 'w', encoding='utf-8').write(str(merge_dict(create_inverted_index())))
    print(f"Time taken: {datetime.datetime.now() - x1}")
