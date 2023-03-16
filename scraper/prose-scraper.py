import requests
import json
from bs4 import BeautifulSoup
from utils import getUrlOfProse

with open('../src/kanda/bala/chapters.json') as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    # for x in json_data:
    # URL = getUrlOfProse(x['kanda'], x['sarga'])
    URL = 'https://www.valmikiramayan.net/utf8/baala/sarga13/bala_13_prose.htm'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find('body')
    for pTag in body.find_all('p', recursive=False, class_=True):
        # if pTag['class'] == ['tat']:
        print(pTag.decode_contents())
