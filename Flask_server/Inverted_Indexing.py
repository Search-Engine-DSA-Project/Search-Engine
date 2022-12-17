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

