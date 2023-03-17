import re
import requests
import json
from bs4 import BeautifulSoup
from utils import getUrlOfProse, cleaner, dumpAsJson

with open('../src/kanda/ayodhya/chapters.json') as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    for index, x in enumerate(json_data):
        if index == 24 or index == 39:
            prose_object = {}
            prose_content = []
            URL = getUrlOfProse(x['kanda'], x['sarga'])
            print(URL)
            # Only for bala
            if index == 24:
                URL = 'https://www.valmikiramayan.net/utf8/ayodhya/sarga25/ayodhya_5F25_prose.htm'
            if index == 39:
                URL = 'https://www.valmikiramayan.net/utf8/ayodhya/sarga40/ayodhya_5F40_prose.htm'
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
                            # prose_object['overview'] = cleaner(
                            #     pTag.text.strip('\n').replace('\n', ''))
                            prose_object['overview'] = cleaner(pTag.decode_contents().strip(
                                '\n').replace('\n', ' ').replace('\u00a0', ' ').replace('\t', ' '))
                        if pTag['class'] == ['tat']:
                            prose_content.append(
                                {'type': 'verse', 'text':  cleaner(pTag.decode_contents().strip('\n').replace('\n', ' ').replace('\u00a0', ' ').replace('\t', ' '))})
                        if pTag['class'] == ['comment']:
                            prose_content.append(
                                {'type': 'commentary', 'text':  cleaner(pTag.decode_contents().strip('\n').replace('\n', ' ').replace('\u00a0', ' ').replace('\t', ' '))})
            except:
                print("Something went wrong")

            prose_object['content'] = prose_content

            # print(prose_content)
            print(x['sarga'])

            dumpAsJson(
                prose_object, f"../src/kanda/ayodhya/prose/chapter/{x['sarga']}.json")
