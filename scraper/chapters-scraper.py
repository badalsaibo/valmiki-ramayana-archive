import requests
from bs4 import BeautifulSoup
from utils import getUrlOfKanda, dumpAsJson, cleaner
# URL = 'https://www.valmikiramayan.net/utf8/baala/sarga14/bala_14_prose.htm'
# URL = 'https://www.valmikiramayan.net/utf8/kish/kishkindha_contents.htm'


# 1. Get all the tags inside the body element
# 2. loop the tags
# 3. if the tag is a p tag with class '.tat'
#     1. extract its text content only
# 4. if the tag is a p tag with class ''

kanda = 'yuddha'

URL = getUrlOfKanda(kanda)
# URL = 'https://www.valmikiramayan.net/utf8/kish/kishkindha_contents.htm'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

body = soup.find('body')

# for pTag in body.find_all('p', recursive=False):

#     if pTag['class'] == ['tat']:
#         print(pTag)

chaptersList = []

for index, tr in enumerate(body.find_all('tr')):
    td = tr.find('td')
    if td:
        splittedName = td.text.strip().split(":")
        print(splittedName)
        chaptersList.append({"id": splittedName[0].strip(), "kanda": kanda, "sarga": splittedName[0].strip(),
                             "chapter": splittedName[0].strip(), "title": cleaner(splittedName[1].strip())})


dumpAsJson(chaptersList, f"../src/kanda/{kanda}/chapters.json")
