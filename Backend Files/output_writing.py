##James Kaufman
##import out packages

import csv
import os
import os.path
import io
import pandas as pd
from pandas import DataFrame, read_csv

#we currently have a 2d list(array)
test = [["Sam", "Tim", "Jon"], ["Elizabeth", "Magnus", "Kazuma"], ["Axelle", "Magdalena", "Geoff"]]
names = ["Sam", "Tim", "Jon", "Elizabeth", "Magnus", "Kazuma", "Axelle", "Magdalena", "Geoff"]
ages = ["21", "45", "32", "13", "16", "20", "24", "25", "67"]

DataSet = list(zip(names, ages))
print(DataSet)

df = pd.DataFrame(data = DataSet, columns = ['Names', 'Ages'])
print(df)

df.to_csv('hi_there.csv',index=False,header=["one", "two"])


#let's write it to a csv file!
# dir = r"C:\Users\13014\Desktop"
#
#
# if not os.path.exists(dir):
#     os.mkdir(dir)
#
# with open(os.path.join(dir, "test"+'.csv'), "w") as f:
#   csvfile=io.StringIO()
#   csvwriter=csv.writer(f)
#   for l in test: #l is each array in test
#       #print("hi")
#       # for x in l:#x is each individual element
#       #     print(x)
#       csvwriter.writerow(l)
#   # for a in csvfile.getvalue():
#   #   f.writelines(a)