text=input("enter the  names")
l1=text.split(" ")
count=0
for i in l1:
    count=count+i.count('a')
print("occurence of a in the list",count)