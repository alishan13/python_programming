st=input("enter the string")
if st.endswith ("ing"):
    st+='ly'
elif len(st)>=3:
    st+='ing'
print(st)