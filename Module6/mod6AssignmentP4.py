import sys
from datetime import datetime 


datetime_object = datetime.now() 

def log_height(feet, inches):
    print(datetime_object.strftime('%Y-%m-%d %H:%M:%S'), "\t", feet, "Foot", inches, "Inches")

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 2:
        feet, inches = data
    log_height(feet, inches)


    
