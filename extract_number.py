#!/usr/bin/env python
# -*- coding: utf-8 -*-


### USE
### python extract_number.py final/final.csv final/twitter.csv

import csv
import sys
from dateutil import parser
from dateutil.relativedelta import relativedelta

twitter_number = {}

with open(sys.argv[1]) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    for row in readCSV:
    	if row[0] == "username":
            continue
    	space_number = row[1].find(' ')
    	date = row[1][0:space_number]
    	if date not in twitter_number:
    		twitter_number[date] = 1
    	else:
    		twitter_number[date] += 1


print "total twitter:", twitter_number

with open(sys.argv[2],"wb") as outfile:
    writer= csv.writer(outfile)
    row = []
    row.append('date')
    row.append('number')
    writer.writerow(row)
    for key in sorted(twitter_number):
        row = []
        row.append(key)
        row.append(twitter_number[key])
        writer.writerow(row)
