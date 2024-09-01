import json

URL_SET = set()
DUMP = "/home/sanjay/Development/personal/gpt-researcher/outputs/dump.json"
DUMP_DATA = "/home/sanjay/Development/personal/gpt-researcher/outputs/content.txt"

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

def update_dump_data(Data):
    with open(DUMP_DATA, "a") as f:
        f.write(Data)

def Add_Compressed_Record(Data):
    update_dump_data(Data)

def Clear_Compressed_Record():
    update_dump_data("")