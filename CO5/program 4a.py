import pandas as pd
#co_list=["Roll No","Student Name","Grade","CO1","CO2","CO3","CO4","CO5"]
df=pd.read_csv("newstudentdetails.csv",usecols=["Roll No","Student Name","CO1"])
print(df)