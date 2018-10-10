##James Kaufman
##import out packages
import csv



##we currently have a 2d list(array)
test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

##let's write it to a csv file!

with open('test.csv', 'wb', newline = '') as csvfile:
    filewriter = csv.writer(csvfile, delimiter = ' ', quotechar = "|, quoting = csv.QUOTE.MINIMAL")
    for x in range(0, len(test)):
        filewiter.writerow(test[x])
