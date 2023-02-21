l1=[1,3,4,7,9,23]
l2=[2,6,7,9,21,6]
print(l1)
print(l2)
"""if len(l1)==len(l2):
    print("list are of same length")
else:
    print("not same length")
sum=0
sum1=0
for i in l1:
    sum=sum+i
print(sum)
for j in l2:
    sum1=sum1+j
print(sum1)"""
if sum(l1)==sum(l2):
    print("both are same")
else:
    print("not same")
l3=[i for i in l1 if i in l2]
if len(l3)>0:
    print("same elements are ",l3)
else:
    print("no same elements")

