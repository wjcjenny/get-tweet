import glob

interesting_files = glob.glob("latest/*.csv") 

header_saved = False
with open('final/final.csv','wb') as fout:
    for filename in sorted(interesting_files):
        with open(filename) as fin:
            header = next(fin)
            if not header_saved:
                fout.write(header)
                header_saved = True
            else:
            	fout.write('\n')
            for line in fin:
                fout.write(line)



# import shutil
# import glob

# #import csv files from folder
# path = r'result'
# allFiles = glob.glob(path + "/*.csv")
# print allFiles
# with open('final.csv', 'wb') as outfile:
#     for i, fname in enumerate(sorted(allFiles)):
#     	print i, fname
#         with open(fname, 'rb') as infile:
#             if i != 0:
#                 infile.readline()  # Throw away header on all but first file
#             # Block copy rest of file from input to output without parsing
#             shutil.copyfileobj(infile, outfile)
#             print(fname + " has been imported.")


# from datetime import date
# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# import pandas as pd

# start_date = date(2018, 05, 26)
# end_date = date(2018, 8, 9)
# daterange = pd.date_range(start_date, end_date)
# print daterange


# for single_date in daterange:
# 	print single_date