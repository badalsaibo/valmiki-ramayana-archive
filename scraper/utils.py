from words import replaceableWords
import json
from pathlib import Path


def getUrlOfProse(kanda, chapter):
    return f"https://www.valmikiramayan.net/utf8/{kanda}/sarga{chapter}/{kanda}_{chapter}_prose.htm"


def getUrlOfKanda(kanda):
    return f"https://www.valmikiramayan.net/utf8/{kanda}/{kanda}_contents.htm"


def cleaner(sentence):
    newSentence = sentence
    for key in replaceableWords:
        # print(key, replaceableWords[key])
        newSentence = newSentence.replace(key, replaceableWords[key])
    # newSentence = newSentence.encode('ascii', 'ignore')
    return newSentence[0].upper() + newSentence[1:]


def dumpAsJson(listToConvert, filePath):
    json_object = json.dumps(listToConvert, indent=4)

    filePath = Path(filePath)
    filePath.parent.mkdir(parents=True, exist_ok=True)
    with filePath.open("w") as outfile:
        outfile.write(json_object)
