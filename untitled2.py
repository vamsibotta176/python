# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:01:10 2020

@author: VBOTTA
"""

class student :
    def __init__(self):
        self .id =1234
        self.name="vamsi"
        self .address="hyd"
    def display(self):
        print("id is:",self.id)
        print("nameis:",self.name)
        print("addis:",self.address)
s=student()
s.display()


class student:
    def __init__(self):
        self.id=1234
        self.name="mohan"
        self.add="ret"
    def display(self):
        print(self.id,self.name,self.add)
s=student()
s.display()

class student:
    def __init__(self):
        self.id=1234
        self.name="vamsi"
        self.add="gty"
    
s=student()
print(s.__dict__)


class student:
    def __init__(self,name,adress,sid):
        self.id=sid
        self.sname=name
        self.saddress=adress
    def displat(self):
        print("id is:",self.id)
        print("name is:",self.sname)
        print("add",self.saddress)
s=student(101,"bgt","poiu")
s.displat()

class student:
    def __init__(x,y,z,a):
        x.id=y
        x.name=z
        x.add=a
    def disp(x):
        print(x.id,x.name,x.add)
s=student(102,"jkl","poi")
s.disp()


class test:
    def __init__(self):
        self.a=10
        self.b=10
        self.c=20
    def m1(self):
        self.d=30
t=test()
t.m1()
print(t.__dict__)
t.e=12
print(t.__dict__)


class test:
    def __init__(self):
        self.a=10
        self.b=10
        self.c=20
    def m1(self):
        del self.c
t=test()
t.m1()
print(t.__dict__)
t1=test()
t1.m1()
t1.d=20
print(t1.__dict__)


class students:
    institute="durga soft"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def info(cls):
        return cls.institute
    
print(students.info())
s=students(20,40,60)
print(s.avg())
s1=students(89,78,69)
print(s1.avg())


class  aartmethic:
    @staticmethod
    def add(x,y):
        print("the sum is:",x+y)
    @staticmethod
    def product(x,y):
        print("product is :",x*y)
        
a=aartmethic()
a.add(2,3)
a.product(4,5)


class student:
    x=10
    def __init__(self):
        self.a=11
        self.b=23
    def m2(self):
        student.x
   
s=student()
s.m2()
print(s.x,s.a,s.b)
s1.student=19
s1=student()
student.x=19
print(s1.x,s1.a,s1.b)


class student:
    def __init__(self):
        a=100
        print(a)
    def display(self):
        b=1000
        print(b)
s=student()
s.display()


class student:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def display(self):
        print (self.x,self.y,self.z)
s=student(101,"vamsi","hyd")
s.display()

class stu:
    x1=10
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def m1(self):
        print(self.x,self.y)
        
t=stu(101,"vamsi")
t.m1()
print(t.x1,t.x,t.y)
stu.x1=20
print(t.x1,t.x,t.y)


class student:
    institute="durga soft"
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def m1(self):
        return(self.x+self.y+self.z)/3
    @classmethod
    def info(cls):
        return cls.institute
print(student.info())
s=student(34,45,67)
s.m1()
print(s.m1())
s1=student(23,45,67)
print(s1.m1())


class arthmethics:
    @staticmethod
    def add(x,y):
        print("sum is:",x+y)
    @staticmethod
    def product(x,y):
        print("product is:",x*y)
a=arthmethics
a.add(7,8)
a.product(4,5)


class employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eno,self.ename,self.esal)
class test:
    def modify(self):
        self.esal=self.esal+2000
        self.display()
        
e=employee(101,"vamsi",10000)
test.modify(e)


import threading 
import time 

l=threading.Lock()
def display(name):
    for i in range(1,5):
        l.acquire()
        print("hello:",end=" ")
        time.sleep(1)
        print(name)
    l.release()
    
t=threading.Thread(target=display,args=("vamsi",))

t.start()
t.join()



import threading
import time

l=threding.Rlock()
def factorial(n):
    for i in range(3):
        l.acquire()
        if n==0:
            print("the factorial is:",1)
        else:
            print("the factorial of th number", num,"is",factorial(n))
        
t=threading.Thread(target=display,args=(5,))

    