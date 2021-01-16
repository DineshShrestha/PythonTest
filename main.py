import argparse
import random
import csv
import numpy as np
import airdistance as ad
import sorting as sd
#Read the file content if random number is as arguments
def readfile(index):
    reader = csv.DictReader(open('places.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)        

    return(dict_list[index])

#Read file content without random number
def readfilecontent():
    reader = csv.DictReader(open('places.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)        
    return(dict_list)


#Adding the optional arguments
parser = argparse.ArgumentParser()
parser.add_argument("n", type=int,
                    help="optional argument n")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = random.randint(0, args.n)
if args.verbose:
    # n is given as input to randomly generate places as input
    readfile(args.n)
    #Function call to find the distance between all pair of places
    ad.airdistance()
    # #Function call to sort distance in ascending order and find the average distance
    sd.sortingFile()
    sd.findAvg()

else:
    readfilecontent()
    #Function call to find the distance between all pair of places
    ad.airdistance()
     #Function call to sort distance in ascending order and find the average distance
    sd.sortingFile()
    sd.findAvg()



