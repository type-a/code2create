import csv

with open('/Users/munish/Desktop/shizz.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile,delimiter=' ', quotechar='|')
    i=0
    y=[]
    for row in reader:
        print row
 
#            x=row[0][:].split(';')
            #x -- > variable with all info and all parameters in an array'''

