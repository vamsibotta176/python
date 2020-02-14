# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:09:45 2020

@author: VBOTTA
"""

ntrems=int(input("how many terms:"))
n1,n2=0,1
count=0
if ntrems<=0:
    print("the number is postive ")
elif ntrems==0:
    print("the no the series")
else:
    while count < ntrems:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count += 1


import math 
p=float(input("please enter the principle of the amount:"))
n=float(input("please ente the years:"))
r=float(input("please enter the  rate:"))
ci=p * (math.pow((1 + r / 100), n))
print(ci)
i=ci-p
print(i)


p=float(input("please enter the principle:"))
n=float(input("please ente the years:"))
r=float(input("please enter the  rate:"))
t=float(input("please enter the terms to pay:"))
ci=p * (((1 + r / 100*t)**n*t))
print(ci)
i=ci-p
print(i)

n= int(input("please entet the number:"))
fact=1

if n<=0:
     print("the number does not have")
elif n==1:
    print("the number have fact  one")
else:
    for i in range(1,n+1):
        fact = fact*i
    print(fact)
        