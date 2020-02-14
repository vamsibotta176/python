# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:46:04 2020

@author: VBOTTA
"""

class student:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def display(self):
        print(self.id,self.name,self.sal)


s=student(101,"vamsi",9000)
s.display()


class car:
    def __init__(self):
        print("outer class")
    class enginee:
        def __init__(self):
            print("inner class")
        def m1(self):
            print("inner class of")
o=car().enginee().m1()

import gc

print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())


class car:
    def __init__(self):
        self.__updatesoftware()
    
    def drive(self):
        print("Driving")
    def __updatesoftware(self):
        print("updating")
c=car()
c.drive()


class car:
    __maxspeed=0
    __name=" "
    def __init__(self):
        self.__maxspeed=200
        self.__name="ford figo"
    def m1(self):
        print("driving")
        print(self.__maxspeed)
        print(self.__name)
    def setspeed(self,speed):
        self.setspeed=speed
        print(self.setspeed)
        
c=car()
c.m1()
c.setspeed(100)
c.m1()



class book:
    def __init__(self,pages):
        self.pages=pages
    def __mul__(self,other):
        return(self.pages*other.pages)
b=book(100)
b1=book(200)
print(b*b1)


class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __mul__(self,other):
        return self.salary*other.days
class timesheets:
    def __init__(self,days,name):
        self.name=name
        self.days=days
        
e=employee("durga",34)
t=timesheets("durga",2080)
print(e*t)


num =625
a=num**0.5
print(a)

import cmath
num=1+2j
print(cmath.sqrt(num))

import time 
def prime_num(n):
    if n==1:
        return False
    for d in range(2,n):
        if n%d==0:
            return False
    return True
t=time.time()
for n in range(0,101):
    print(n,prime_num(n))
t1=time.time()
print(t1-t)


import math 
import time 
def prime_num(n):
    if n==1:
        return False 
    max_divisors=math.floor(math.sqrt(n))
    for d in range(2,1+max_divisors):
        if n%d==0:
            return False
        return True
for n in range(1,21):
    print(n,prime_num(n))
    
    
import math 
import time 
def prime_num(n):
    if n==1:
        return False
    if n==2:
        return True
    if n>2 and n%2==0:
        return False
    max_divisors=math.floor(math.sqrt(n))
    for d in range(3,1+max_divisors):
        if n%d==0:
            return False
        return True
for n in range(1,21):
    print(n,prime_num(n))

num =97
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("the is not prime number",num)
            print(i,"times",num//i, "is",num)
            break
    else:
        print("the prime number")
else:
    print("is not a prime number")
    
    
lower =1
upper =100
print("the prime",lower,"and",upper)
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
           print(num)
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = 320
print_factors(num)



def computehcf(x,y):
    if x>y:
        smaller =x
    else:
        smaller =y
    for i in range(1,smaller+1):
        if (x%i==0) and (y%i==0):
            hcf=i
    return hcf
num1=12
num2=14
print(computehcf(num1,num2))




def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
num1=12
num2=14
print(gcd(num1,num2))



def compute_lcm(x,y):
    if x>y:
        greater=y
    else:
        greater=x
    while True:
        if(greater%x==0) and (greater%y==0):
          lcm=greater
          break
        greater+=1
    return lcm
num1=12
num2=90
print(compute_lcm(num1,num2))


def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x

def compute_lcm(x,y):
    while y:
        lcm=x*y//gcd(x,y)
    return x
num1=12
num2=90
print(compute_lcm(num1,num2))