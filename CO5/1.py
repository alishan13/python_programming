'''fl_obj=open("sample.txt",'r')
rl=fl_obj.readlines()
print("File line by line in list:")
print(rl)

print("\n\n")
#to remove newline characters
rl=[x.strip() for x in rl]
print("File line by line in list,post removing newline:")
print(rl)
fl_obj.close()'''

print([line.strip() for line in open("sample.txt",'r')])
