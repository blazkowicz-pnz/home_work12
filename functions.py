import json
PATH = "posts.json"
def read_from_json(PATH):
    with open(PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

__data = read_from_json(PATH)


def search_in_post(word):
    posts = []  #список постов, в которых содержится подстрока "word"
    for d in __data:
        if str(word).lower() in d["content"].lower():
            posts.append(d)
    return posts


def dump_content_in_json(content):
    with open(PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
        data.append(content)
        with open(PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)
    return data




