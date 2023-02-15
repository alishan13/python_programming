import pandas as p
std_f=p.read_csv("Students Detail.csv",usecols=["Name","Address"])
print("Student name and address : ")
print(std_f)

'''
import pandas as p
std_f=p.read_csv("Students Detail.csv")
#specific column
spec_col=std_f[["Name","Roll No."]]
print("Student Name and Roll.No:")
print(spec_col)
'''
