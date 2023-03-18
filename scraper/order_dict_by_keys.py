import json
from utils import dumpAsJson

ordered_list = ['id', 'kanda', 'sarga',
                'title', 'chapter', 'overview', 'content']


kanda = 'ayodhya'

with open(f'../src/kanda/{kanda}/chapters.json') as json_file:

    json_data = json.load(json_file)

    for index, x in enumerate(json_data):
        with open(f'../src/kanda/{kanda}/prose/chapter/{x["sarga"]}.json') as chapter_json_fle:
            chapter_json_list = json.load(chapter_json_fle)
            # print(chapter_json_list)
            d = chapter_json_list      # dictionary containing key-value pairs that are to be ordered
            l = ordered_list  # list of keys that represent the order for the dictionary
            # retrieve the values in order and build a list of ordered key-value pairs
            ordered_dict_items = [(k, d[k]) for k in l]
            # print(ordered_dict_items)
            dumpAsJson(ordered_dict_items,
                       f'../src/kanda/{kanda}/prose/chapter/{x["sarga"]}.json')
