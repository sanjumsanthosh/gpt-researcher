import json

URL_SET = set()
DUMP = "/home/sanjay/Development/personal/gpt-researcher/outputs/dump.json"

def update_dump(URL_list):
    with open(DUMP, "w") as f:
        f.write(json.dumps(URL_list, indent=4))

def Add_URL(URLs):
    if type(URLs) == list:
        for URL in URLs:
            URL_SET.add(URL)
    else:
        URL_SET.add(URLs)
    update_dump(list(URL_SET))

def CLEAR_URL():
    URL_SET.clear()
    update_dump(list(URL_SET))