# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:12:07 2019

@author: VBOTTA
"""
frist ="vicky"
second ="vamsi"
word= (frist+' '+second)
print(word[0])

x=float(input("please enter the numbers:"))
y=x*x+200
print(y)

x=int(input("please enter the numbers:"))
y=x*x+200
print(y)

q=7 // 3
print(q)

r =7%3 
print(r)

name=input("what is your name\n")
print(name)

prompt="what is the speed of the vehicle\n"
speed =input(prompt)
v = int(speed)+int(input("please enter the number:"))
print(v)

words=(10,100,30)
for word in words:
    print(word)

pizza=("what is the perctange of the  acheived")
for slice in pizza:
    print(slice)
    
p=int(input("please enter the numbers:"))
r=int(input("please enter the numbers:"))/100
t=int(input("please enter the numbers:"))
ins = p*r*t
print(ins)
amount = p+ins
print(amount)

x=input("enter your name:")
print("Hello",x)

y=float(input("Enter the hours:"))
z=float(input("Enter the rate:"))
hrs = (y*z)
print(hrs)
year =hrs*52
print(year)


width= 234
height =456
print((width*height)//2)
print((width*height)%2)
print((width*height)//2.0)


z=float(input("Please enter the  temperature in the clesuis:"))
d= (z*(9/5))+32
print(d)