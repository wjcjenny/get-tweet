# -*- coding: utf-8 -*-

# import sys
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
# import os
import time
import subprocess
import pandas as pd



def main():
	start_date = date(2018, 05, 26)
	end_date = date(2018, 8, 9)
	daterange = pd.date_range(start_date, end_date)
	print daterange


	for single_date in daterange:
		day_plus = single_date + relativedelta(days=1)
		outputFileName  = 'top/top-' + str(single_date.strftime("%Y-%m-%d")) + ".csv"
		print outputFileName
		print("Collecting tweets beetwin", single_date.strftime("%Y-%m-%d"), " to ", day_plus.strftime("%Y-%m-%d"), "for", outputFileName)
		subprocess.check_output(['python','Exporter.py', '--querysearch', '#WalkAway', '--since', single_date.strftime("%Y-%m-%d"), '--until', day_plus.strftime("%Y-%m-%d"), '--output', outputFileName, '--toptweets'])
	print "DONE"

main()