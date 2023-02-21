class time:
    def __init__(self):
        self.h=int(input("enter the hours"))
        self.m=int(input("enter the minutes:"))
        self.s=int(input("enter the seconds"))
    def __add__(self,obj2):
        hours=self.h+obj2.h
        print("sum of hours",hours)
        minutes=self.m+obj2.m
        print("sum of minutes",minutes)
        second=self.s+obj2.s
        print("sum of seconds",second)
        if hours>24:
            hours=hours%24
        if minutes>60:
            hours=hours+minutes//60
            minutes=minutes%60
        if second>60:
            minutes=minutes+second//60
            second=seconds%60
        return hours,minutes,second
print("enter the first time")
t1=time()
print("enter the second time:")
t2=time()
print(t1+t2)
