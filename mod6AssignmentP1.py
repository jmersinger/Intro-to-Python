###Libaries###
import sys

#Adding datetime library
from datetime import datetime

#Given code
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
    
    #Add datetime.now() to print statement to log when the data is entered
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "{0}\t{1}".format(item, cost))




    