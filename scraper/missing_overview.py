import json
from utils import dumpAsJson

kanda = 'ayodhya'

with open(f'../src/kanda/{kanda}/chapters.json') as json_file:

    json_data = json.load(json_file)

    for index, x in enumerate(json_data):
        with open(f'../src/kanda/{kanda}/prose/chapter/{x["sarga"]}.json') as chapter_json_fle:
            chapter_json_list = json.load(chapter_json_fle)

            if "overview" in chapter_json_list:
                print("Exists")
            else:
                print(f"Does not exist {chapter_json_list['sarga']}")
                # print(chapter_json_list['content'][0]['text'])
                chapter_json_list['overview'] = chapter_json_list['content'][0]['text']
                new_content = chapter_json_list['content']
                # print(new_content)
                del new_content[0]
                chapter_json_list.update({'content': new_content})
                dumpAsJson(
                    chapter_json_list, f'../src/kanda/{kanda}/prose/chapter/{x["sarga"]}.json')
