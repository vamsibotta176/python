# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("hello world")
a=int(input("please enter the the number:"))
b=int(input("please enter the number:"))
c=a+b
d=a-b
e=a*b
f=a/b
g=a//b
h=a%b
print("sum of the numbers",c,"subraction of the numbers",d,"multiplication of the numbers",e,"Division of the numbers",f,"qutioent of the number",f,"remainder of the number",h)

def add_numbers(x,y):
   numbers = x + y
   return numbers

num1 =int(input("please enter the the number:"))
num2 =int(input("please enter the number:"))

print("The sum is", add_numbers(num1, num2))

def mur_numbers(x,y):
    numbers = x-y 
    return numbers
num1= int(input("please enter the numbers:"))
num2=int(input("please enter the numbers:"))
print("The subract is",mur_numbers(num1, num2))

def mult_numbers(x,y):
    numbers=x*y
    return numbers
num1= int(input("please enter the numbers:"))
num2= int(input("pleaae enter the numbers:"))
print("the multplication is",mult_numbers(num1,num2))

def div_numbers(x,y):
    numbers = x/y
    return numbers
num1=int(input("please enter the numbers:"))
num2=int(input("please enter the numbers:"))
print("the division of ",div_numbers(num1,num2))


n= input("please enter the numbers:")
n = int(n)
sum = 0
avg =0
for num in range(0,n+1,1):
    sum=sum+num
    avg=sum/n
    print("the number is",n,"the sum of the number", sum,"the average ofthe numbers",avg)
print("the number is",n,"the sum of the number", sum,"the average ofthe numbers",avg)
    
sum=0
avg =0
list=[11,22,33,44,55,66,77]
for num in list:
    sum= sum +num
    avg =sum/len(list)
print("the sum of the number",sum,"the avg of the list",avg)

n =int(input("please enter the numbers:"))
total_numbers = n
sum=0
while (n >= 0):
    sum += n
    n-=1
print ("sum using while loop ", sum)
average  = sum / total_numbers
print("Average using a while loop ", average)

list =[10,20,30,40,50,60,10,90]
print(list)
print(type(list))

list=[]
print(list)
print(type(list))

set ={10,20,30,40,50,60,70,89}
print(set)
print(type(set))

tuple=10,20,30,40,50,60,70,80
print(tuple)
print(type(tuple))

a={10,}
print(a)
print(type(a))

b=(10,)
print(b)
print(type(b))

n = int(input("please enter the number:"))
for i in range(0,n):
    t=i*i
    b=i*i*i
    print("the number is:",i,"the square of the number is:",t,"the cube of the number is :",b)
    
print("The numbers between 0 t0 6")
for i in range(0,6):
    print(i)

print("double of the numbers from the range")
for i in range(5):
    print(i*i,end=",\n")
    
print("All the even numbers:")
for i in range(0,10,2):
    print(i,end=',\n')
    
start = 10
stop= 100
step=10
stop+=step
for i in range(start,stop,step):
    print(i,end=", \n")

start = -20
stop= 20
step=-2
stop+=step
for i in range(start,stop,step):
    print(i,end=",")
import numpy as np

A=np.array([[2,3,4],[7,5,6],[10,8,9]])
print(A)
print(type(A))
print(A.size)
print(A.shape)
print(A.ndim)
print(A.max())
print(A.min())
print(A.dtype)
print(A.flatten())

import numpy 
A=numpy.zeros((6,6))
print(A)
A=numpy.ones(7)
print(A)

b=numpy.array((1,2,3,4))
print(b)
print(type(b))
print(b.dtype)
c=numpy.full((1,2),6,dtype="complex")
print(c)
print(type(c))

d=numpy.random.random((8,8))
print(d)

e=numpy.logspace(20,2,30)
print(e)

f=numpy.linspace(20,5,30)
print(f)