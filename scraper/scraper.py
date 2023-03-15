import requests
from bs4 import BeautifulSoup

# URL = 'https://www.valmikiramayan.net/utf8/baala/sarga14/bala_14_prose.htm'
URL = 'https://www.valmikiramayan.net/utf8/baala/baala_contents.htm'

page = requests.get(URL)


def getUrlOfProse(chapter):
    return f"https://www.valmikiramayan.net/utf8/baala/sarga{chapter}/bala_{chapter}_prose.htm"


def getUrlOfKanda(kanda):
    return f"https://www.valmikiramayan.net/utf8/{kanda}/{kanda}_contents.htm"


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
    print(index)
    if index == 10:
        continue
    if td:
        splittedName = td.text.strip().split(".")
        print(splittedName)
        balaKanda.append({"id": splittedName[0], "sarga": splittedName[0],
                         "chapter": splittedName[0], "title": splittedName[1].strip()})

print(balaKanda)
