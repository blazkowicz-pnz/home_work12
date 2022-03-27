import json
from config import PATH


def dump_content_in_json(content):
    with open(PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
        data.append(content)
        with open(PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)
    return data