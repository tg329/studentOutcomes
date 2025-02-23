import csv
import re


# convert percentages rates into decimals to d3 can do the percentage conversion itself
def convertRates(row):
    row['Young workers'] = float(row['Young workers']) / 100.0
    row['All workers'] = float(row['All workers']) / 100.0
    row['Recent graduates'] = float(row['Recent graduates']) / 100.0



# import and run passes_filter
data = []
header = []

with open('unemployed.csv','r') as f:
    reader = csv.DictReader(f)
    
    header = reader.fieldnames
    for row in reader:
        convertRates(row)
        data.append(row)

print(len(data))

# export to new CSV       
with open('unemployed-filtered.csv','w', newline = '') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
