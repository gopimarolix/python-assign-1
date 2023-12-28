#from leena import x
#print(x)

#from leena import x
#import leena
#print(leena.x)
#leena.add(10,20)
#leena.pro(4,2)

#import leena as l
#print(l.x)
#l.add(10,20)
#l.pro(4,5)

#from leena import x,add,pro
#print(x)
#add(10,20)
#pro(4,5)

#from leena import *
#print(x)
#add(10,20)
#pro(4,5)

#from leena import x as a,add as b,pro as c
#print(a)
#b(10,5)
#c(3,4)

#import leena,pandu
#print(pandu.r)


#import time
#import leena

#print("the program is entering into the sleep mode",leena.x)
#time.sleep(30)
#import leena
#print("this is last line of program",leena.x)


import time
from imp import  reload
import leena

print("program entering into the sleep mode",leena.x)
time.sleep(30)
reload(leena)
print("this is last line of program",leena.x)
