s=input("enter the string:")
subs=input("enter the sub string:")
flag=False
position=-1
n=len(s)
while True:
    position=s.find(subs,position+1,n)
    if position==-1:
     break
    print("found at index:",position)
    flag=True
    if flag==False:
        print("Not found")