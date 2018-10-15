##James Kaufman
##import our packages
import csv
import os
import os.path
import io
import pandas as pd
from pandas import DataFrame, read_csv

##Create two mock columns for the spreadsheet
names = ["Sam", "Tim", "Jon", "Elizabeth", "Magnus", "Kazuma", "Axelle", "Magdalena", "Geoff"]
ages = ["21", "45", "32", "13", "16", "20", "24", "25", "67"]
##Create our list
DataSet = list(zip(names, ages))
##Specify the column names
dataColumns = ['Names', 'Ages']
##Create the DataFrame
df = pd.DataFrame(data = DataSet, columns = dataColumns)
##Convert the DataFrame to a CSV file in the file directory
df.to_csv('hi_there.csv',index=False,header=dataColumns)