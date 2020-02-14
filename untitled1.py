# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:33:30 2019

@author: VBOTTA
"""

print("hello world")
name="vamsi"
print("hello:",name)

def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mult(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
def floor(x,y):
    return(x//y)
def quo(x,y):
    return(x%y)
def w(x,y):
    return(x*y)
def wer(x,y):
    return(x**y)

print("please enter the number:")
print("1.add")
print("2.sub")
print("3.mult")
print("4.div")
print("5.floor")
print("6.quo")
print("7.w")
print("8.wer")

choice=input("plese enter the choice(1/2/3/4/5/6/7/8):")
    
num1=int(input("please enter the number:"))
num2=int(input("please enter number:"))
if choice=="1":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice =="2":
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice=="3":
    print(num1,"*",num2,"=",mult(num1,num2))
elif choice=="4":
    print(num1,"/",num2,"=",div(num1,num2))
elif choice=="5":
    print(num1,"//",num2,"=",floor(num1,num2))
elif choice=="6":
    print(num1,"%",num2,"=",quo(num1,num2))
elif choice=="7":
    print(num1,"*",num2,"=",w(num1,num2))
elif choice=="8":
    print(num1,"**",num2,"=",wer(num1,num2))
else:
    print("invalid input")



    

    