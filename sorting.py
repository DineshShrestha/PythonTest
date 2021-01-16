import csv
import os
import pandas as pd
import sys
import importlib
importlib.reload(sys)

if os.path.exists('output.csv'):
    os.remove('output.csv') #this deletes the file
else:
    print("The file does not exist")#add this to prevent errors
# write the sorted file in ascending order
def sortingFile():
    reader = csv.DictReader(open('calcDistance.csv', 'r'))
    result = sorted(reader, key=lambda d: float(d['Distance']))

    writer = csv.DictWriter(open('output.csv', 'w'), reader.fieldnames)
    writer.writeheader()
    writer.writerows(result)


# Find the average distance on the csv file and displaying the value
def findAvg():    
    sum =0
    count =0
    avg =0
    lst=[]
    close =0
    with open('output.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lst.append(float(row["Distance"]))
            sum += float(row["Distance"])
            count +=1
        avg=sum/count    
    # Placing pair and corresponding distance closest to average value
        close = min(enumerate(lst), key=lambda x: abs(x[1]-avg))
        print("Average is {}km. Someplace : {} - Otherplace : {}  - {} km.".format(avg, row['Someplace'], row['Otherplace'], close))
