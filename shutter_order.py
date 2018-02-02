#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodecsv as csv

allList = []

with open('shutter_count_2.csv', 'rb') as f:
    reader = csv.reader(f)
    rows = list(reader)

    i = 0
    for r in rows :
        i += 1
        if i == 1 :
            continue
        d = {"q":r[0],"count":int(r[1])}
        allList.append(d)



newList = sorted(allList, key=lambda k: k['count'])
# print newList

with open('shutter_count_order_2.csv', 'a') as csvfile:
    w = csv.writer(csvfile)
    
    for i,d in enumerate(newList) :
        if i == 0 :
            w.writerow(["q", "count"])
        w.writerow([d["q"], d["count"]])

    csvfile.flush()



        