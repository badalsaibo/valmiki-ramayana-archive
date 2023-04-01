import re
import requests
import json
from bs4 import BeautifulSoup
from utils import getUrlOfProse, cleaner, dumpAsJson


def decoder(htmlTag):
    return cleaner(htmlTag.decode_contents(None, 'utf-8', 'html').strip(
        '\n').replace('\n', ' ').replace('\u00a0', ' ').replace('\t', ' '))


kanda = 'yuddha'

# chapters.json contains all chapters of a particular kanda
# loop through all these chapters
# for each chapter
# use the kanda and sarga to determine the URL
# request the URL
# parse the content
# save everything to dict prose_object
# output prose_object as a json

with open(f'../src/kanda/{kanda}/chapters.json') as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    for index, x in enumerate(json_data):
        # if index == 0:
        prose_object = {}
        prose_content = []
        URL = getUrlOfProse(x['kanda'], x['sarga'])
        print(URL)
        # index 24 and 25 have _5F_ added on the URL
        if index == 24:
            URL = f'https://www.valmikiramayan.net/utf8/{kanda}/sarga25/yuddha_5F25_prose.htm'
        if index == 39:
            URL = f'https://www.valmikiramayan.net/utf8/{kanda}/sarga40/yuddha_5F40_prose.htm'
        prose_object['id'] = f"prose-{x['kanda']}-{x['sarga']}"
        prose_object['kanda'] = x['kanda']
        prose_object['sarga'] = x['sarga']
        prose_object['title'] = x['title']
        prose_object['chapter'] = x['chapter']
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        body = soup.find('body')

        try:
            for pTag in body.find_all('p',  class_=True):
                if (not len(pTag.text.strip())):
                    continue
                if len(pTag.contents) > 0:
                    if pTag['class'] == ['txt']:
                        prose_object['overview'] = decoder(pTag)
                    if pTag['class'] == ['tat']:
                        prose_content.append(
                            {'type': 'verse', 'text':  decoder(pTag)})
                    if pTag['class'] == ['comment']:
                        prose_content.append(
                            {'type': 'commentary', 'text': decoder(pTag)})
        except:
            print("Something went wrong")

        prose_object['content'] = prose_content

        # print(prose_content)
        print(x['sarga'])

        dumpAsJson(
            prose_object, f"../src/kanda/{kanda}/prose/chapter/{x['sarga']}.json")
