import re
import requests
import json
from bs4 import BeautifulSoup
from utils import getUrlOfProse, cleaner, dumpAsJson


def decoder(htmlTag):
    return cleaner(htmlTag.decode_contents(None, 'utf-8', 'html').strip(
        '\n').replace('\n', ' ').replace('\u00a0', ' ').replace('\t', ' '))


with open('../src/kanda/aranya/chapters.json') as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    for index, x in enumerate(json_data):
        # if index == 1:
        prose_object = {}
        prose_content = []
        URL = getUrlOfProse(x['kanda'], x['sarga'])
        print(URL)
        # Only for bala
        if index == 24:
            URL = 'https://www.valmikiramayan.net/utf8/aranya/sarga25/aranya_5F25_prose.htm'
        if index == 39:
            URL = 'https://www.valmikiramayan.net/utf8/aranya/sarga40/aranya_5F40_prose.htm'
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
            prose_object, f"../src/kanda/aranya/prose/chapter/{x['sarga']}.json")
