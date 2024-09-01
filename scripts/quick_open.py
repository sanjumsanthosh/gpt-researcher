JSON_PATH="/home/sanjay/Development/personal/gpt-researcher/outputs/dump.json"

import json
import webbrowser
from icecream import ic

def GetLinksAndSort(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    data = list(set(data))
    data.sort()
    return data

def OpenInBrowser(link):
    webbrowser.open(link)

Links = GetLinksAndSort(JSON_PATH)

print("Found " + str(len(Links)) + " links")

i = 0
while i < len(Links):
    link = Links[i]
    print("Press enter to open link " + str(i+1) + "/" + str(len(Links)) + " - " + link + ", press a to skip all from same domain, press n to go to next link, press q to quit")
    inp = input()
    if inp == 'q':
        break
    elif inp == 'a':
        domain = link.split('/')[2]
        print("Skipping all links from domain " + domain)
        while i < len(Links) and Links[i].split('/')[2] == domain:
            i += 1
    elif inp == 'n':
        i += 1
        continue
    else:
        OpenInBrowser(link)
        print("Opened " + link)
        i += 1

