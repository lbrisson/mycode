#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/"

new_animal= {
           "name": "Owl",
           "desc": "Extremelt smart & talented hunter",
           "abilities": ["fly","hunt","night vision"]
          }

# json.dumps takes a python object and returns it as a JSON string
new_animal= json.dumps(new_animal)

# requests.post requires two arguments at the minimum;
# a url to send the request 
# and a json string to attach to the request
resp= requests.post(URL, json=new_animal)


# pretty-print the response back from our POST request
pprint(resp.json())

