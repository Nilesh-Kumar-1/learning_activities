
class car:
    wheel=4
    def __init__(self):
        self.name="Nilesh"

    def get_name(self):
        return self.name
    # this is example of instance method

    @classmethod
    #class method is to fetch class variables
    def info(cls):
        return cls.wheel
    
    @staticmethod
    def other():
        print("this is static method")

a=car()
b=car()

print(a.name,b.name,a.wheel,b.wheel)
a.other()
print(a.info())

a.wheel=5
print(a.name,b.name,a.wheel,b.wheel)

car.wheel=5
print(a.name,b.name,a.wheel,b.wheel)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# create outer class
class Doctors:
	def __init__(self,name,name2):
		self.name = name
		self.den = self.Dentist(name2)
		self.car = self.Cardiologist()

	def show(self):
		print('In outer class')
		print('Name:', self.name)

	# create a 1st Inner class
	class Dentist:
		def __init__(self,name2):
			self.name = name2
			self.degree = 'BDS'

		def display(self):
			print("Name:", self.name)
			print("Degree:", self.degree)

	# create a 2nd Inner class
	class Cardiologist:
		def __init__(self):
			self.name = 'Dr. Amit'
			self.degree = 'DM'

		def display(self):
			print("Name:", self.name)
			print("Degree:", self.degree)


# create a object
# of outer class
outer = Doctors("nilesh","nils")
outer.show()

# create a object
# of 1st inner class
d1 = outer.den

# create a object
# of 2nd inner class
d2 = outer.car
print()
d1.display()
print()
d2.display()


        

#inheretance

class A:
	wheel=5
	def __init__(self):
		self.name="Nilesh"

class B(A):
	pass

class C(B):
	pass

test=C()
test2=B()
test3=C()
A.wheel=9
print(id(test),id(test2),id(test3))
a=int()

print(test.name,C.wheel, test.wheel)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# operator overloading



class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __str__(self):
        return f"{self.m1}, {self.m2}"

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Studet(m1, m2)

    def __gt__(self, other):
        return (self.m1 + self.m2) > (other.m1 + other.m2)
	
a=Student(10,23)
b=Student(23,45)
print(a+b)

# Method overriding
class Info:
	def __init__(self) -> None:
		self.name="nilesh"
	def printname(self):
		print("Name is Nilesh")
class Infos(Info):
	def printname(self):
		print ("Name is Nileshh")

#method overloading		

#encapsulation

# As a naming convention we can use "_" to protect the method/attributes
# Where as __ is used for private members

class encap:
	def __init__(self) -> None:
		self.a="Nilesh"
		self.__c="kumar"
		self._b="Nilesh Kumar 12"
	def __add(self,other):
		return self.a+ self.__c
	
	def prints(self):
		return self.__c
	
Encap=encap()
# print(Encap.__add(2))
# print(Encap.__c)
print(f"{Encap.prints()} is value of Encap.__c")
print(Encap._b)
Encap._encap__c="23"
print(Encap._encap__c) #Name managling
print(Encap._encap__add(2))

# Data abstraction

# Import required modules 
from abc import ABC, abstractmethod 
# Abstract method of base class force its child class to write the implementation of the all abstract methods
# defined in base class. If we do not implement the abstract methods of base class in the child class then 
# our code will give error.
# Create Abstract base class 
class Car(ABC): 
	def __init__(self, brand, model, year): 
		self.brand = brand 
		self.model = model 
		self.year = year 
	
	# Create abstract method	 
	@abstractmethod
	def printDetails(self): 
		pass
		
	# Create concrete method 
	def accelerate(self): 
		print("speed up ...") 
		
	def break_applied(self): 
		print("Car stop") 
	
# Create a child class 
class Hatchback(Car): 
	
	def printDetails(self): 
		print("Brand:", self.brand); 
		print("Model:", self.model); 
		print("Year:", self.year); 
		
	def Sunroof(self): 
		print("Not having this feature") 
	
# Create a child class 
class Suv(Car): 
	
	def printDetails(self): 
		print("Brand:", self.brand); 
		print("Model:", self.model); 
		print("Year:", self.year); 
		
	def Sunroof(self): 
		print("Available") 

	
car1 = Hatchback("Maruti", "Alto", "2022"); 

car1.printDetails() 
car1.accelerate() 
	
# class int:
# 	def __init__(self,a) -> None:
# 		self.a=a
# 	def __str__(self):
# 		return "122"
# 	def __add__(self,b):
# 		return f'345'+str({b})

test1=int(12)
test2=int(13)
test3=test1+test2
print(test3.__add__(45))
