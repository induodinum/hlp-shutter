#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json





charList = list("abcdefghijklmnopqrstuvwxyz")

for i in charList :
    for j in charList:
        q = i + j
        url = "http://www.shutterstock.com/api/autocomplete?q=" + q + "&mediaType=image"
        req = requests.get(url)
        j = json.loads(req.text)
        data = j["data"]
        autocompletions = data["autocompletions"]
        for auto in autocompletions :
            pattern = auto["pattern"]
            print (pattern)


        
