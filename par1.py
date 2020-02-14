# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:57:41 2020

@author: VBOTTA
"""

n=int(input("please enter the number is:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("the number is  not prime number")
            print(i,"times",n//i,"number",n)
            break 
    else:
            print("the number is  prime number")
else:
    print("the number is not prime",n)
    
lower = int(input("please enter the number:"))
upper = int(input("please enter the number:"))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
def is_primenumber(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for n in range(1,21):
    print(n,is_primenumber(n))
import math
import time 
def is_primenuber(n):
    if n==1:
        return False
    max_divisiors=math.floor(math.sqrt(n))
    for i in range(2,1+max_divisiors):
        if n%i==0:
            return False
    return True
t0=time.time()
for  n in range(1,100):
    print(n,is_primenuber(n))
t1=time.time()
print(t0-t1)


import time
import math 
def is_primenuber(n):
    if n==1:
        return False
    if n ==2:
        if n>2 and n%2==0:
            return True
    max_divisors =math.floor(math.sqrt(n))
    for  i in range(3,1+max_divisors,2):
        if n%i==0:
            return False
    return True
for n  in range(1,21):
    print(n,is_primenuber(n))
    
    
num=int(input("please enter the number:"))
fact=1
if num<0:
    print("there is no factorial")
elif num==0:
    print("the fact is one")
else:
    for i in range(1,num+1):
        fact =fact*i
    print("the fact of the number",num,"is",fact)
    
num =int(input("please enter the nuber:"))
for i in range(1,110):
    print(num,"x",i,"=",num*i)