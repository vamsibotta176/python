# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:19:23 2019

@author: VBOTTA
"""

a=100

def add(x,y):
    print("the sum of the nuber is :",x+y)
    
    
def mul(x,y):
    print("the mul of the two numbers is:",x*y)


def div(x,y):
    print("the division of the number is:",x/y)



def compute_hcf(x,y):
    if x>y:
        smaller =y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if(x%i==0) and (y%i==0):
            hcf=i
    return hcf
num1=14
num2=21
print("the hcf of the numbers is :",compute_hcf(num1,num2)) 

def compute_hcf(x,y):
    while(y):
        x,y=y,x%y
    return x
num1=14
num2=21
print("the hcf of the numbers is:",compute_hcf(num1,num2))


def compute_lcm(x,y):
    if x>y:
        greater=y
    else:
        greater=x
    while True:
        if(greater%x==0) and (greater%y==0):
            lcm =greater
            break
        greater +=1
    return lcm
num1=14
num2=21
print("lcm of the two numbers is:",compute_lcm(num1,num2))

def compute_hcf(x,y):
    while(y):
        x,y=y,x%y
    return x
def compute_lcm(x,y):
    lcm=x*y//compute_hcf(x,y)
    return lcm
num1=14
num2=21
print("lcm:",compute_lcm(num1,num2))


import numpy 
a=numpy.array([1,2,3,43,4,5,6])
print(type(a))
print(a.size)
print(a.dtype)
print(a.ndim)

a=numpy.linspace(1,20,3)
print(a)
a=numpy.logspace(1,10,5)
print(a)
a=numpy.ones(5,int)
print(a)
a=numpy.zeros(5,int)
print(a)
a=numpy.arange(1,20,5)
print(a)


from array import *
d=array("i",[])

n=int(input("please enter te number is:"))

for i in range(n):
    x=int(input("enter the next:"))
    d.append(x)
print(d)


import array
a=array.array("i",[])
n=int(input("please enter the number is:"))
for i in range(n):
    x=int(input("please enter the next value:"))
    a.append(x)
print(a)
s=int(input("please search the  number:"))
print(a.index(s))

s=[]
n= int(input("please entet the number:"))
for i in range(n):
    x= int(input("please enter th numbers:"))
    s.append(x)
print(s)

import numpy
a=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(type(a))
print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype)

import numpy
a=numpy.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(a)
print(type(a))
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.shape)
print(a.max())
print(a.min())
print(a.sum())
print(a.max(axis=1))
print(a.max(axis=0))
print(a.min(axis=1))
print(a.min(axis=0))
b=numpy.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(a*b)
print(a*a)
print(b*b)

b=a.flatten()
print(b)

import numpy
a=numpy.array([[1,2,3],[4,5,6],[7,8,9]],"float")
print(a)
print(a.size)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(type(a))

print(a+3)
print(a*2)
print(a**2)

a=numpy.linspace(1,10,2)
print(a)
a=numpy.logspace(2,10,2)
print(a)




import numpy 
a=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.shape)
print(type(a))
print(a.max())
print(a.min())
print(a.max(axis=0))
print(a.max(axis=1))
print(a.min(axis=0))
print(a.min(axis=1))
print(a.astype("float"))
print(type(a))
c=(numpy.copy(a))
print(c)
b=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

import numpy as np
a=np.array([0,np.pi/2,np.pi])
print(np.sin(a))
b=np.array([0,np.pi/4,np.pi/3])
print(np.cos(b))


lower = 1
upper = 100
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
lower=1
upper=100
print("Prime numbers",lower,"and",upper)
for num in range(lower,upper+1):
    if (num%2==0) or (num%2==0) or(num%5==0) or(num%7==0) or(num%11==0):
        pass
    else:
        print(num)
        
        
lower=1
upper=500
print("prime numbrers",lower,"and",upper)
for num  in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            print(num)
            

year=2002

if(year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print("the year is {0}".format(year))
        else:
            print("the year is not leap year".format(year))
    else:
            print("th year is leap year".format(year))
else:
    print("the year is  not a leap year {0}".format(year))
            
    
num=4
factorial=1
if num<0:
    print("sooory there is no fatorial")
elif num==0:
    print("the factorial is  1")
else:
     for i in range(1,num+1):
         factorial=factorial*i
     print("the factorial of the num",num,"is",factorial)
     
     
def print_factor(x):
    print("the factors of the",x,"are:")
    for i in range(1,x+1):
        if x%i==0:
            print(i)
num=320
(print_factor(num))


num=5
factorrial =1 
if n<0:
    print("there is no factorial")
elif n==0:
    print("the ffactorial is:",factorial)
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of the num",num,"is",factorial)
    
    
    
def compute_hcf(x,y):
    if x>y:
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if(smaller%i==0) and (smaller%i==0):
            hcf =i
    return hcf
num1=12
num2=24
print(compute_hcf(num1,num2))

def compute_hcf(x,y):
    while(y):
        x,y=y,x%y
    return x

def compute_lcm(x,y):
    if x>y:
        greater=y
    else:
        greater=x
    while True:
        if (greater%x==0) and (greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm
num1=12
num2=13
print(compute_lcm(num1,num2))

def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
def compute_lcm(x,y):
    lcm=x*y//gcd(x,y)
    return lcm
num1=1
num2=2
print(compute_lcm(num1,num2))


import random 
for i in range(10):
    print(random.random())
    
import random
for i in range(10):
    print(random.randint(1,10))
    
import random
for i in range(10):
    print(random.uniform(1,10))
    
import random
for i in range(10):
    print(random.randrange(10))