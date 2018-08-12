
# from dateutil import parser
# from dateutil.relativedelta import relativedelta
# dt = parser.parse("2018-08-02 01:39")

# print dt-relativedelta(hours=3)


#!/usr/bin/env python
# -*- coding: utf-8 -*-


### USE
### python extract_twitter_num.py final/final.csv final/twitter.csv

import csv
import sys
from dateutil import parser
from dateutil.relativedelta import relativedelta

twitter_name_time = []

with open(sys.argv[1]) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    for row in readCSV:
    	if row[0] == "username":
            continue

        dt = parser.parse(row[1])
        dt_3 = dt - relativedelta(hours=3)

        row_str = row[0] + ' ' + str(dt_3)
        print row_str
        if row_str not in twitter_name_time:
        	twitter_name_time.append(row_str)


# print "twitter_name_time:", twitter_name_time

twitter_number = {}

for key in twitter_name_time:
	date = key.split(' ')
	# print date

	if date[1] not in twitter_number:
		twitter_number[date[1]] = 1
	else:
		twitter_number[date[1]] += 1

# print "total twitter:", twitter_number


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


