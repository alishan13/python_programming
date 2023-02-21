f=open('new1.txt','r')
lines=[]
for line in f:
   lines.append(line.strip('\n'))
print(lines)
