
import csv as c
csv_fl=open("Students Detail.csv")
csv_read=c.reader(csv_fl)

for line in csv_read:
    print(line)
