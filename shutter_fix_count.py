#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodecsv as csv


import requests
import json
import time

token = "1/eyJjbGllbnRfaWQiOiI5NDBhMjUzMmZjZTY4YzVmNWM1YiIsInJlYWxtIjoiY3VzdG9tZXIiLCJzY29wZSI6InVzZXIudmlldyB1c2VyLmVkaXQgY29sbGVjdGlvbnMudmlldyBjb2xsZWN0aW9ucy5lZGl0IGxpY2Vuc2VzLnZpZXcgbGljZW5zZXMuY3JlYXRlIGVhcm5pbmdzLnZpZXcgbWVkaWEudXBsb2FkIG1lZGlhLnN1Ym1pdCBtZWRpYS5lZGl0IHB1cmNoYXNlcy52aWV3IHJlc2VsbGVyLnZpZXcgcmVzZWxsZXIucHVyY2hhc2UiLCJ1c2VybmFtZSI6InNhcmFucG9sIiwidXNlcl9pZCI6MTQ1Njg0ODU2LCJvcmdhbml6YXRpb25faWQiOm51bGwsImN1c3RvbWVyX2lkIjo0MDYyNjk4MCwiZXhwIjoxNDc4ODA2NDY1fQ.W779thiHh74DYzK56D6b3xzYa-aFMRb-1U1CwoiHQmuIgaGU4oU_kbC2PvOzzNTgqiaoEgXlMlwXtRU2zSfReg"


headers = {'Content-Type': 'application/json',
            'Accept-Charset': 'UTF-8',
            'Authorization': 'Bearer ' + token}



def getCount(i, q) :
    print i
    print q
    reqText = ""
    try:
        url = "https://api.shutterstock.com/v2/images/search?&per_page=1"
        url += "&license[0]=commercial"
        url += "&license[1]=editorial"
        url += "&license[2]=enhanced"
        url += "&license[3]=sensitive"
        url += "&license[4]=NOT enhanced"
        url += "&license[5]=NOT sensitive"
        url += "&query=" + q 
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


with open('shutter_count_2.csv', 'a') as csvfile:
    w = csv.writer(csvfile)
    
    with open('shutter_count.csv', 'rb') as f:
        reader = csv.reader(f)
        rows = list(reader)

        i = 0
        for r in rows :
            i += 1
            if i == 1 :
                w.writerow(["q", "count"])
                continue
            
            q = r[0]
            count = r[1]
            if count == "0" :
                count = getCount(i, q)
                print count

            w.writerow([q, count])
            csvfile.flush()



        