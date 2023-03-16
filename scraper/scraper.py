import requests
import json
from bs4 import BeautifulSoup
from pathlib import Path

# URL = 'https://www.valmikiramayan.net/utf8/baala/sarga14/bala_14_prose.htm'
URL = 'https://www.valmikiramayan.net/utf8/baala/baala_contents.htm'

page = requests.get(URL)

replaceableWords = {
    'rAma': 'Rama',
    'vashiSTa': 'Vasishtha',
    'vashiSTHa': 'Vasishtha',
    'nArada': 'Narada',
    'vAlmIki': 'Valmiki',
    'vAmana': 'Vamana',
    'vishvamitra': 'Vishvamitra',
    'vishvAmitra': 'Vishvamitra',
    'trishanku': 'Trishanku',
    'janaka': 'Janaka',
    'shiva': 'Shiva',
    'ikshvaaku': 'Ikshvaku',
    'bharata': 'Bharata',
    'sItha': 'Sita',
    'vishnu': 'Vishnu',
    'brahma': 'Brahma',
    'rAmAyaNa': 'Ramayana',
    'dasaratha': 'Dasharatha',
    'dasharatha': 'Dasharatha',
    'tATaka': 'Tataka',
    'kaartikeya': 'Kaartikeya',
    'putrakAmeShTi': 'Putrakameshti',
    'vashiShTha': 'Vasishtha',
    'lakshmaNa': 'Lakshmana',
    'deomoness': 'demoness',
    'kapila': 'Kapila',
    'bhageeratha': 'Bhageeratha',
    'ganga': 'Ganga',
    'ahalya': 'Ahalya',
    'shunashshepa': 'Shunashshepa',
    'shatrughna': 'Shatrughna',
    'sarayu': 'Sarayu',
    'amshuman': 'Amshuman'

}


def getUrlOfProse(chapter):
    return f"https://www.valmikiramayan.net/utf8/baala/sarga{chapter}/bala_{chapter}_prose.htm"


def getUrlOfKanda(kanda):
    return f"https://www.valmikiramayan.net/utf8/{kanda}/{kanda}_contents.htm"


def cleaner(sentence):
    newSentence = sentence
    for key in replaceableWords:
        # print(key, replaceableWords[key])
        newSentence = newSentence.replace(key, replaceableWords[key])
    return newSentence[0].upper() + newSentence[1:]


def dumpAsJson(listToConvert, filePath):
    json_object = json.dumps(listToConvert, indent=4)

    filePath = Path(filePath)
    filePath.parent.mkdir(parents=True, exist_ok=True)
    with filePath.open("w") as outfile:
        outfile.write(json_object)


# 1. Get all the tags inside the body element
# 2. loop the tags
# 3. if the tag is a p tag with class '.tat'
#     1. extract its text content only
# 4. if the tag is a p tag with class ''
soup = BeautifulSoup(page.content, 'html.parser')

body = soup.find('body')

# for pTag in body.find_all('p', recursive=False):

#     if pTag['class'] == ['tat']:
#         print(pTag)

balaKanda = []

for index, tr in enumerate(body.find_all('tr')):
    td = tr.find('td')
    if index == 10:
        continue
    if td:
        splittedName = td.text.strip().split(".")
        balaKanda.append({"id": splittedName[0], "sarga": splittedName[0],
                         "chapter": splittedName[0], "title": cleaner(splittedName[1].strip())})


dumpAsJson(balaKanda, "../src/kanda/bala/chapters.json")
