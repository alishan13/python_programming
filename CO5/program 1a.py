#Write a Python program to read a file line by line and store it into a list
f=open('new1.txt','r')    
Lines=f.readlines()
l1=[line.strip() for line in Lines]
print(l1)
