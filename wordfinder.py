#!/usr/bin/env python

import sys
import subprocess
import json
import requests

def show_help():
    command = "cat $HOME/4-permanent/scripts/wordfinder/help.txt"
    subprocess.check_call(command, shell=True)

if len(sys.argv) > 1:
    query = sys.argv[1]
else:
    show_help()
    sys.exit(0)

if query == "--help":
    show_help()
    sys.exit(0)

list_mode = False
if "=" not in query:
    query = "sp=" + query
else:
    list_mode = True
    parameter, value = query.split("=")
    if len(parameter) == 3:
        query = "rel_" + query

url = "https://api.datamuse.com/words?{}&md=d".format(query)
response = requests.get(url)
results = json.loads(response.text)
result = {
    "word": query,
    "defs": ["No definition found"],
}

if "sp=" in query and not list_mode:
    for r in results:
        if "defs" in r:
            result = r
            break
    word = result["word"]
    definitions = result["defs"]
    print(word)
    for definition in definitions:
        print(definition)
else:
    print(query)
    for result in results:
        print(result["word"])

