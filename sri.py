#s="gopi is a good boy"
#print(s.startswith("gopi"))
#print(s.endswith("gopi"))

name='aman'
age=34
salary=1000
print("{}'s age is {} and his salary is {}".format(name,age,salary))
print("{0}'s age is {2} and his salary is {1}".format(name,age,salary))
print("{z}'s age is {x} and his salary is {y}".format(z=name,x=age,y=salary))