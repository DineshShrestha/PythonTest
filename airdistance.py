import pandas as pd
import numpy as np
import csv
from math import radians, cos, sin, asin, sqrt
import os
if os.path.exists('calcDistance.csv'):
    os.remove('calcDistance.csv') #this deletes the file
else:
    print("The file does not exist")#add this to prevent errors

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km 

    
# skip the first header row from the file
def airdistance():    
    places = pd.read_csv("places.csv", skiprows=0)
    with open('calcDistance.csv', 'w') as csv_file:
        fieldnames = ['Someplace', 'Otherplace', 'Distance']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0,len(places)):  
            for j in range(0,len(places)):
                if i==j:
                    break
                else:
                    #Function call to calculate the air distance
                    distance = haversine(places.Longitude[i],places.Latitude[i],places.Longitude[j],places.Latitude[j])
                    writer.writerow({'Someplace': places.Name[i], 'Otherplace': places.Name[j], 'Distance': distance})
                    print("-----------------------------------------------------------------------------------------------")
                    print("| Someplace: {} | Otherplace: {} | Distance(km): {}".format(places.Name[i],places.Name[j], distance))
                   
 

