# TODO: Creating Inverted Indexing:
#   1. Create a function inverted indexing (Done)
#   2. Inverted Indexing details:
#       a. Importing Lexicon and Forward_Indexing (Done)
#       b. Using Lexicon to identify the unique words (Done)
#       c. Using Forward_Indexing to map documents according to those unique words (Done)

from Parsing import json_parser


def inverted_index(path):
    lexicon_forward_index = json_parser(path)
    inverted_indexing = {i: {} for i in lexicon_forward_index[0]}
    for doc_id, tokens in lexicon_forward_index[1].items():
        for token in tokens:
            if doc_id in inverted_indexing[token]:
                inverted_indexing[token][doc_id] += 1
                continue
            inverted_indexing[token][doc_id] = 1
    return inverted_indexing

