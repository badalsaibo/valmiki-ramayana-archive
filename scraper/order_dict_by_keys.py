import json
from utils import dumpAsJson

ordered_list = ['id', 'kanda', 'sarga',
                'title', 'chapter', 'overview', 'content']


kanda = 'bala'

with open(f'../src/kanda/{kanda}/chapters.json') as json_file:

    json_data = json.load(json_file)

    for index, x in enumerate(json_data):
        with open(f'../src/kanda/{kanda}/prose/chapter/{x["sarga"]}.json') as chapter_json_fle:
            chapter_json_list = json.load(chapter_json_fle)
            # https://stackoverflow.com/a/70985799/7679903
            ordered_dict = {}
            for item in ordered_list:
                ordered_dict[item] = chapter_json_list[item]

            # print(ordered_dict_items)
            dumpAsJson(ordered_dict,
                       f'../src/kanda/{kanda}/prose/chapter/{x["sarga"]}.json')
