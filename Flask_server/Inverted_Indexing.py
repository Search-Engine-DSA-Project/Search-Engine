# TODO: Creating Inverted Indexing:
#   1. Create a function inverted indexing (Done)
#   2. Inverted Indexing details:
#       a. Importing Lexicon and Forward_Indexing (Done)
#       b. Using Lexicon to identify the unique words (Done)
#       c. Using Forward_Indexing to map documents according to those unique words (Done)

from Lexicon import create_lexicon
from Forward_Indexing import forward_index
import pandas as pd
import numpy as np


def inverted_index(path):
    lexicon = create_lexicon(path)
    forward_indexing = forward_index(path)
    inverted_indexing = {i: [] for i in lexicon}

    for doc_id, tokens in forward_indexing.items():
        for token in tokens:
            if doc_id not in inverted_indexing[token]:
                inverted_indexing[token].append(doc_id)
    return inverted_indexing

# def inverted_index(path):
#     ##
#     lexicon = create_lexicon(path)
#     df_lexicon = pd.DataFrame(lexicon, columns=['word'])
#     df = forward_index(path)
#     ##
#     # print(type(df))
#     # df = df.to_dict()
#     # print(df.shape())
#     # for row, row2 in df.items():
#     #     # dftemp = pd.DataFrame(row2)
#     #     df_temp = df_lexicon.set_index("word").to_dict()["dummy"]
#
#     df_lexicon["dummy"] = np.nan
#     for row, row2 in df.items():
#         dftemp = pd.DataFrame(row2, columns=["word"])
#         dftemp = dftemp["word"].value_counts()
#         print(row, row2)
#         for col, col2 in dftemp.items():
#             print(col, col2)
#             df_lexicon["dummy"] = {row: col2}
#             print(df_lexicon)
#             # print(dftemp)
#         # df_lexicon.loc[df_lexicon['word'] == col, 'count'] = col2
#         # df_lexicon['count'] = df_lexicon['word'].map(dftemp)
#
#         #     print(df_lexicon)
#         #
#         # print(dftemp)
#         # break
