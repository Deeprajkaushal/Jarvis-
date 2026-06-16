'''
class employee:
  #  name="deep"
    age=21
    salary=1200000
    def dex(self):
        print("the salary is:",self.salary)

@staticmethod
def greet():
    print("welcome to the company")

greet()
employee.dex(employee())
deep=employee()
print(deep.age)
print(deep.salary)

ajay=employee()
print(ajay.age)

ajay.salary=2000000
print(ajay.salary )
'''

'''

class programmer:
    company="microsoft" 
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getInfo(self):
        print(f"the name of the programmer is {self.name} and the product is {self.product}")


deep=programmer("deep","windows")
kalu=programmer("kalu","linux")
deep.getInfo()
kalu.getInfo()
'''
'''
class programmer:
    company="microsoft"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

p=programmer("deep",1200000,)
print(p.name,p.salary,p.company)
    '''
'''

class calculator:
    def __init__ (self,num):
        self.num=num

    def square(self):
        print(f"the square of {self.num} is {self.num**2}")

    def cube(self):
        print(f"the cube of {self.num} is {self.num**3}")

    @staticmethod
    def greet():
        print("welcome to the calculator")

a=calculator(4)
a.greet()
a.square()    
a.cube()


class deep:
    a=4

o=deep()
o.a=0
print(o.a)
'''
'''
from random import randint


class train:
    def __init__(self,trainno,fro,to):
        self.trainno=trainno
        self.fro=fro
        self.to=to

    def bookticket(self):
        print(f"your ticket is booked from {self.fro} to {self.to} with train number {self.trainno}")

    def getstatus(self):
        print(f"the train number is {self.trainno} and it is going from {self.fro} to {self.to}")

    def getfare(self):
        print(f"the fare for the train number {self.trainno} is {randint(100,500)}")


train=train(74092,"delhi","mumbai")
train.bookticket()
train.getstatus()
train.getfare()




class student:
    language="python"
    def show(self):
        print("welcome to the student class")


class teacher(student):
    subject="maths"
    def show(self):
        print("welcome to the teacher class")

class person(teacher):
    def show(self):
        print(f"language: {self.language}, subject: {self.subject}")
        print("welcome to the person class")

a=person()
a.show()
'''

'''
class a:

    a=3
class b(a):

    b=4    
class c(b):

    c=5


k=a()
print(k.a)

m=b()
print(m.a,m.b)  

n=c()
print(n.a,n.b,n.c)  ''''''

class twodvector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        print(f"the x and y coordinates are {self.x} and {self.y}")
    

class threedvector(twodvector):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z

    def show(self):        
        super().show()
        print(f"the z coordinate is {self.z}")

v1=twodvector(1,2)
v2=threedvector(1,2,4)
v1.show()
v2.show()
'''


