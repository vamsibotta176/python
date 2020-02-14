# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:32:37 2019

@author: VBOTTA
"""

import sample

print(sample.a)
(sample.add(3,4))
(sample.mul(2,4))


import sample as s
print(s.a)
s.add(2,3)
s.mul(6,7)

from sample import *
print(a)
add(2,3)
mul(5,6)

from sample import a,add,mul
print(a)
add(2,3)
mul(9,8)


from sample import a as s,add as b,mul as y
print(s)
b(2,4)
y(4,5)


from sample import a,add,mul,div
print(a)
add(2,4)
mul(6,7)
div(10,2)

import sample,sample1
print(sample.a)
print(sample1.a1)
sample.add(2,4)
sample1.per(7,8)
sample1.rty(6,5)
sample.div(30,6)

from sample import *
from sample1 import *
print(a)
print(a1)
add(3,4)
mul(9,8)
div(4,5)
per(6,4)
rty(16,7)
rew(20,5)

dir(str)
help(str)

import math 
print(math.pi)
print(math.ceil(34.5))
print(math.floor(34.5))
print(math.sin(5))
print(math.cosh(56))





g=9
def f1():
    g=10
    print(g)
    print(globals()["g"])
f1()




def f1():
    if __name__=="__main__":
        print("the code is excuted as program")
    else:
        print("the code executed as module some othe rprogram")

f1()
from random import *
for i in range(10):
    print(random())
    
from  random import *
for i  in range(10):
    print(randint(1,10))
    
from random import *
for i in range(10):
    print(uniform(1,100))
    
from random import *
for i in range(10):
    print(randrange(1,100))
from random import *
for i in range(10):
    print(uniform(1,100))
    
from random import *
lst=["vamsi","mohan","siva"]
for i in range(10):
     print(choice(lst))    
     
import datetime
x=datetime.datetime.now()
print(x)

import datetime
x=datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)


import datetime
x=datetime.datetime(2010,4,5)
print(x)

import datetime
x=datetime.datetime(2015,6,7)
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%B"))
print(x.strftime("%b"))
print(x.strftime("%Y"))
print(x.strftime("%y"))


import calendar
yy=2000
mm=12
print(calendar.month(yy,mm))


import datetime 
x=datetime.datetime.today()
print(x)


import datetime
print(dir(datetime))


import datetime
x=datetime.date(2019,12,29)
print(x)

from datetime import date
x=datetime.date(2019,3,4)
print(x)

from datetime import date
x=date.today()
print(x)


from datetime import date
x=date.fromtimestamp(1326244364)
print(x)


from datetime import date
x=date.today()
print(x.year)
print(x.month)
print(x.day)


from datetime import time
x=time()
print(x)

x=time(2,10)
print(x)

x=time(2,10,45,3456)
print(x)

from datetime import time 
x=time(11,23,45)
print(x.hour)
print(x.minute)
print(x.second)


from datetime import datetime
x=datetime(2023,5,6)
print(x)

x=datetime(2023,4,5,11,23,45,876)
print(x)
print(x.hour)
print(x.minute)
print(x.second)
print(x.day)
print(x.month)
print(x.year)
print(x.timestamp())


import array

A= array.array("i",[1,2,3,4])
print(A)
print(type(A))
print(A.typecode)
print(A.buffer_info())
A.append(34)
print(A)
print(len(A))
A.remove(A[3])
print(A)

A.reverse()
print(A)


import array as arr
A=arr.array("i",[1,2,3,4,5])
print(A)
for i in range(len(A)):
    print(A[i])
B=arr.array("i",(i*i*i for i in A))
print(B)

c=arr.array(A.typecode,(i for i in A))
print(c)


import array as arr
a=arr.array("i",[1,2,3,4,5])
print(a)
print("the new array created :",end=" ")
for i in range(0,3):
    print(a[i],end=" ")
print()


import array as arr
b=arr.array("f",[1,2,3,5,6])
print(b)
for i in range(len(b)):
    print(b[i],end=" ")
print()


import array as arr
c=arr.array("i",[1,2,3,4,5])
print(c)
print("the new array created:",end=" ")
for i in range(len(c)):
    print(c[i],end=" ")
print()
c.insert(1,4)
print("the new array created:",end=" ")
for i in range(len(c)):
    print(c[i],end=" ")
print()





import array as arr
d=arr.array("f",[1,2,3,4,5])
print(d)
print("the new rray created:",end=" ")
for i in range(len(d)):
    print(d[i],end=" ")
print()

d.insert(5,6)
print("the new array created:",end=" ")
for i in range(len(d)):
    print(d[i],end=" ")
print()


import array as  arr
e=arr.array("i",[1,2,3,5,6,7,8])
print(e)
print("Acess the element is:",d[0])

print("cess  the element is:",d[1])


import array as arr
a=arr.array("i",[1,2,3,4,5,6])
print(a)
print("the new aray is created:",end=" ")
for i in range(len(a)):
    print(a[i],end=" ")
print("\r")

print("the popped the element:",end=" ")
print(a.pop(2))


import array as arr
b=arr.array("i",[1,2,3,4,5])
print(b)
print("the new array is created:",end=" ")
for i in range(len(b)):
    print(b[i],end=" ")
print()
b.remove(1)
print("the removing eement:",end=" ")
for i in range(0,3):
    print(b[i],end=" ")
print()


import array as arr
b=arr.array("i",[1,2,3,4,5,6])
print(b)
print("the new array is created :",end=" ")
for i in range(len(b)):
    print(b[i],end=" ")
print()
print("the element remove  fro the array:",end=" ")
b.remove(1)
for i in range(len(b)):
    print(b[i],end=" ")   
print()


import array as arr
b=arr.array("i",[1,2,3,4,5,6,7,8])
print(b)
print("the elements created:",end=" ")
for i in range(len(b)):
    print(b[i],end=" ")
    
print()
print("the element is removed:",end=" ")
b.remove(1)
for i in range(len(b)):
    print(b[i],end=" ")
    
print()



import array as arr
b=arr.array("i",[1,2,3,5,4])
print(b)
print("the elements created:",end=" ")
for i in range(len(b)):
    print(b[i],end=" ")
print()
print("the element is add:",end=" ")
b.append(8)
for i in range(len(b)):
    print(b[i],end=" ")
print()


import array as arr
c=[1,2,3,4,5,6,7,8,9,10]
a=arr.array("i",c)
print(a)
for i in range(len(a)):
    print(a[i],end=" ")
    sliced_arr=a[3:8]
    print("\n silicing element in a range 3-8:")
    print(sliced_arr)
    sliced_arr=a[5:]
    print("\n slicing the array range 5:")
    print(sliced_arr)
    sliced_arr =a[:]
    print("\n print all the elements using the slice:")
    print(sliced_arr)
    
    
import array as arr
a=arr.array("i",[1,2,3,4,5,6,7,8,9])
for i in range(len(a)):
    print(a[i],end=" ")
print("\r")
a[2]=90
print("Array after update:",end=" ")
for i in range(len(a)):
    print(a[i],end=" ")
   