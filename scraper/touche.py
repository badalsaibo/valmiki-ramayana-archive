import re
import requests
import json
from bs4 import BeautifulSoup
from utils import getUrlOfProse, cleaner, dumpAsJson

with open('../src/kanda/bala/chapters.json') as json_file:

    json_data = json.load(json_file)

    for index, x in enumerate(json_data):
        with open(f'../src/kanda/bala/prose/chapter/{x["sarga"]}.json') as chapter_json_fle:
            chapter_json_list = json.load(chapter_json_fle)

            chapter_json_list['title'] = x['title']

            dumpAsJson(chapter_json_list,
                       f"../src/kanda/bala/prose/chapter/{x['sarga']}.json")
