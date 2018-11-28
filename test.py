import csv

csvFile = open('productDescriptions.csv', 'r')
next(csvFile)
read = csv.reader(csvFile)

for row in read:
    d = row[1]
    print(d)