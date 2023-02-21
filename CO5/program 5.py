#Write a Python program to write a python dictionary to a csv file .
#After writing the csv file read the csv file and display the content.

#program to write a python dictionary to a csv file
import csv
#creating a list of field names
#field_names=['No.','Company','Model']

#creating list of python dictionaries
cars=[{'No.':1,'Company':'Ferrari','Model':'488GTB'},{'No.':2,'Company':'BMW','Model':'BMWX7'},{'No.':3,'Company':'Porsche','Model':'918spyder'}]
csvfile=open('Names.csv','w')

field_names=list(cars[0].keys())

writer=csv.DictWriter(csvfile,fieldnames=field_names)

writer.writeheader()
writer.writerows(cars)
csvfile.close()

csv_file=open('Names.csv','r')
csv_reader=csv.reader(csv_file)
#print (csv_reader)
for line in csv_file:
    print (line,end="")
