from Inverted_Indexing import inverted_index
import multiprocessing
import datetime
import os


def create_inverted_index():
    dataset = os.listdir(path)

    with multiprocessing.Pool(processes=6) as p:
        __inverted_list__ = p.map(inverted_index, [(path + x) for x in dataset])
    return __inverted_list__


def merge_dict(merge_list):
    dict1 = {}
    for item in merge_list:
        for key, value in item.items():
            if key in dict1:
                dict1[key] += value
            else:
                dict1[key] = value
    return dict1


if __name__ == '__main__':
    path = '.\\temp_testing\\'
    x1 = datetime.datetime.now()
    # open('.\\Dataset\\Output_test\\output_test.json', 'w', encoding='utf-8'). \
    #     write(str(merge_dict(create_inverted_index())))
    merge_dict(create_inverted_index())
    print(f"Time taken: {datetime.datetime.now() - x1}")
