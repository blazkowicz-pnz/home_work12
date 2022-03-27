import json
from config import PATH


def read_from_json(PATH):
    with open(PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def search_in_post(word):
    posts = []  #список постов, в которых содержится подстрока "word"
    data = read_from_json(PATH)
    for d in data:
        if str(word).lower() in d["content"].lower():
            posts.append(d)
    return posts