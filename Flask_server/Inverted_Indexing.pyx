from Parsing import json_parser



# def inverted_index(path):
#     lexicon_forward_index = json_parser(path)
#     inverted_indexing = {i: {} for i in lexicon_forward_index[0]}
#     for doc_id, tokens in lexicon_forward_index[1].items():
#         for token in tokens:
#             if doc_id in inverted_indexing[token]:
#                 inverted_indexing[token][doc_id] += 1
#                 continue
#             inverted_indexing[token][doc_id] = 1
#     return inverted_indexing
# @numba.jit
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
    print("at inverted indexing")
    return inverted_indexing



# import datetime
# import os
# from Inverted_Indexing import inverted_index
# from collections import defaultdict, Counter
# from concurrent.futures import ProcessPoolExecutor
# import multiprocessing
#
#
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
#
#
# if __name__ == '__main__':
#     # 'X:\\Dataset\\nela-gt-2021\\newsdata\\'
#     path = ".\\temp_testing\\"
#     x1 = datetime.datetime.now()
#     open('.\\output_test.json', 'w', encoding='utf-8').write(str(merge_dict(create_inverted_index())))
#     print(f"Time taken: {datetime.datetime.now() - x1}")


#
#
# def inverted_index(path):
#     # Create an inverted index for the data in a single file
#     lexicon, doc_dict = json_parser(path)
#     index = defaultdict(Counter)
#     for doc_id, tokens in doc_dict.items():
#         for token in tokens:
#             index[token][doc_id] += 1
#     return index
#
#
# def create_inverted_index(path):
#     # Create an inverted index for all the data in the given directory
#     indexes = []
#     for file in os.listdir(path):
#         indexes.append(inverted_index(path + file))
#     # Merge the inverted indexes into a single index
#     merged_index = defaultdict(Counter)
#     for index in indexes:
#         for token, doc_counts in index.items():
#             merged_index[token] += doc_counts
#     return merged_index
#
#
# # def create_inverted_index(path):
# #     # Create an inverted index for all the data in the given directory
# #     with ProcessPoolExecutor() as executor:
# #         indexes = list(executor.map(inverted_index, (path + x for x in os.listdir(path))))
# #     # Merge the inverted indexes into a single index
# #     merged_index = defaultdict(Counter)
# #     for index in indexes:
# #         for token, doc_counts in index.items():
# #             merged_index[token] += doc_counts
# #     return merged_index
#
#
# if __name__ == '__main__':
#     path = ".\\temp_testing\\"
#     # Create the inverted index
#     x1 = datetime.datetime.now()
#     index = create_inverted_index(path)
#     # Save the inverted index to a JSON file
#     with open('.\\output_test.json', 'w', encoding='utf-8') as f:
#         json.dump(index, f)
#     print(f"Time taken: {datetime.datetime.now() - x1}")


# import os
# import json
# import spacy
# from concurrent.futures import ProcessPoolExecutor
# from collections import defaultdict, Counter
# import pandas as pd
#
# # Load spacy model
# nlp = spacy.load('en_core_web_md')
#
# def json_parser(path):
#     def temp_parse(x):
#         # Tokenize and lemmatize the input string
#         doc = nlp(x)
#         tokens = [token.lemma_ for token in doc if not token.is_stop]
#         return tokens
#     # Load JSON data and apply temp_parse to each element of the 'content' column
#     with open(path, 'r') as f:
#         df = pd.DataFrame(json.load(f))
#     df['content'] = df['content'].apply(temp_parse)
#     # Extract unique tokens and create a dictionary mapping doc IDs to token lists
#     unique_tokens = set(token for doc in df['content'].values for token in doc)
#     doc_dict = {row['id']: row['content'] for row in df.to_dict(orient='records')}
#     return unique_tokens, doc_dict