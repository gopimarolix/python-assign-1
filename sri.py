a=[10,20,30,40,50]
b=a
print(id(a))
print(id(b))
print(b)

x=["dog","cat","lion","tiger"]
y=["dog","cat","lion","tiger"]
print(x is y)

l=(10,20,30,40)
print(type(l))

l=int(input("enter the numbers:"))
total=l
sum=0
while l >= 0:
    sum +=l
    l-=1
    print("sum =",sum)
    avg=sum/total
    print("average =",avg)
    
s={10,20,30} 
l=[999,333,222,111]
s.update(l)
print(s)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

t=[56,44,33,21,2]
print(len(t))
print(t.count(44))
print(t.index(33))
print(t.index(300))
print(sorted(t))
print(t.sort())
t.sort()
print(t)