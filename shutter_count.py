#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time

token = "1/eyJjbGllbnRfaWQiOiI5NDBhMjUzMmZjZTY4YzVmNWM1YiIsInJlYWxtIjoiY3VzdG9tZXIiLCJzY29wZSI6InVzZXIudmlldyB1c2VyLmVkaXQgY29sbGVjdGlvbnMudmlldyBjb2xsZWN0aW9ucy5lZGl0IGxpY2Vuc2VzLnZpZXcgbGljZW5zZXMuY3JlYXRlIGVhcm5pbmdzLnZpZXcgbWVkaWEudXBsb2FkIG1lZGlhLnN1Ym1pdCBtZWRpYS5lZGl0IHB1cmNoYXNlcy52aWV3IHJlc2VsbGVyLnZpZXcgcmVzZWxsZXIucHVyY2hhc2UiLCJ1c2VybmFtZSI6InNhcmFucG9sIiwidXNlcl9pZCI6MTQ1Njg0ODU2LCJvcmdhbml6YXRpb25faWQiOm51bGwsImN1c3RvbWVyX2lkIjo0MDYyNjk4MCwiZXhwIjoxNDc4NzUyMDgzfQ.d0BaorilEjkk31TiJig079UWubQzRF-cbZARJ42ZhY0PRb_Abi5_BJBr6K6SOle-MVLtheEAkXrffsk3b_769w"


headers = {'Content-Type': 'application/json',
            'Accept-Charset': 'UTF-8',
            'Authorization': 'Bearer ' + token}



def getCount(i, q) :
    print i
    print q
    reqText = ""
    try:
        url = "https://api.shutterstock.com/v2/images/search?per_page=1&query="+ q +"&view=full"
        req = requests.get(url, headers=headers)
        reqText = req.text
        ja = json.loads(reqText)
        return ja["total_count"]
    except Exception as e:
        print "#### ERROR"
        print reqText
        print e
        time.sleep(1) 
        return getCount(i,q)



q_list = [line.rstrip('\n') for line in open('./output/shutter_2.txt')]


import unicodecsv as csv
with open('shutter_count.csv', 'a') as csvfile:
    w = csv.writer(csvfile)
    
    for i,q in enumerate(q_list) :
        if i < 4859 :
            continue
        if i == 0 :
            w.writerow(["q", "count"])
        w.writerow([q, getCount(i,q)])
        csvfile.flush()




        