fl_obj=open("sample.txt",'r')
wl_obj=open("new.txt",'w')
rl=fl_obj.readlines()
for line in range(0,len(rl)):
    if line%2!=0:
        wl_obj.write(rl[line])
wl_obj.close()
wl_obj=open("new.txt",'r')
rl_new=wl_obj.read()
print(rl_new)
wl_obj.close()
fl_obj.close()
