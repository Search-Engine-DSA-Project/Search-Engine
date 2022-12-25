from Parser import json_parser


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
    return inverted_indexing
