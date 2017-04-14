import csv
xx = open("months.txt", "w" )
xx.truncate();
with open('/Users/munish/Desktop/newpp.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile,delimiter=' ', quotechar='|')
    i=0
    y=[]
    for row in reader:
        y.append(row[0].split(','))
a=input()#latitude
b=input()#longitude
c=input()#month
n=0
sunlight=180-a+b#algorithm to find nth latitude and lingitude
print (y[sunlight][c+1]) 

    #'''if (row[2] == 2) or (row[3] == 2'''
  #      i=i+1
#        if(i>12):
#            x=row[0][:].split(';')
            #x -- > variable with all info and all parameters in an array'''
#            if(x[2]=='13'):
#                print x[5] 
#                xx.write(x[5])
#                xx.write(';')
#            y.append(x)

xx.close()
#yy=open("months.txt","r")
#print yy.readlines();
#yy.close();
