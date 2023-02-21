import time
print("current time",time.time())
print("current local time",time.ctime())
print("time after 30 seconds",time.time()+30)
t=time.localtime()
print("year",t.tm_year)
print("month",t.tm_mon)
print("day",t.tm_mday)
print("hr",t.tm_hour)