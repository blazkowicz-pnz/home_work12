import json
PATH = "posts.json"
def read_from_json(PATH):
    with open(PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

__data = read_from_json(PATH)




def search_in_post(word):
    for d in __data:
        if str(word).lower() in d["content"].lower():
            return d

