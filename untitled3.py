# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:34:22 2020

@author: VBOTTA
"""

print("hello world")
name="vamsi"
print("hello:",name)

a=float(input("please enter the  length of the base:"))
b=float(input("please entet the length of the height:"))
area=0.5*a*b
if area<0:
    print("thee is no area")
else:
    print(area)
    
a=float(input("please enter the length of the rectangle:"))
b= float(input("please enter the breadth of the rectangle:"))
area=a*b
if area<0:
    print("there is no area")
else:
    print(area)
    
a=float(input("please enter the length of the  square:"))
area= a*a
print(area)
import math
r=float(input("please the radius the circle:"))
h= float(input("please enter the height of the cylinder:"))
suf =2*3.14*r*(h+r)
csa=2*3.14*r*h
volume =3.14*r*r*h
print(suf)
print(csa)
print(volume)
surf=4*3.14*r*r
print(surf)
volu=1.33*3.14*r*r*r
print(volu)
l=math.sqrt(r*r+h*h)
print(l)
lat=3.14*r* math.sqrt(r*r+h*h)
print(lat)
bas=3.14*r*r
print(bas)
volum =0.668*r*r*h
print(volum)