import datetime
import os
from Inverted_Indexing import inverted_index


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
