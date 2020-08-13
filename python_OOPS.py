# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:47:21 2020

@author: Vinay Borhade
"""

class Humanoid:
    
    species = "Humanoid"
    
    def __init__(self, name, surname, dob, language):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.language = language
        
    def get_full_name(self):
        return(self.name + " " + self.surname)
        
    def get_age(self):
        pass
        
    def mother_tounge(self):
        print("My Mother tounge is ", self.language)
        
    def summary(self):
        print("Hello! my name is ", self.get_full_name())
        print("My age is ", self.get_age())
        print("I belong to species ", self.species)
        
    def sing(self, song):
        print("I am singing the song ", song)
        
        
h1 = Humanoid("Vinay", "Borhade", "30-04-1982", "Marathi")     
    
h1.name
h1.surname
h1.age

h1.mother_tounge()

h1.get_full_name()

h1.summary()


class Human(Humanoid):
    
    def __init__(self, name, surname, dob, language):
        super().__init__(name, surname, dob, language)
    
    def climb(self):
        print("Sorry I cant climb a tree")
        
    def drive(self, vehicle):
        print("I can drive a ", vehicle)
    
human1 = Human("Vinay", "Borhade", "30-04-1982", "Marathi")   
human1.summary()
human1.drive("Car")


class Chimpangee(Humanoid):
    
    def __init__(self, name, surname, dob, language):
        super().__init__(name, surname, dob, language)
        
    def climb(self):
        print("I can climb a tree")
        
    def drive(self, vehicle):
        print("Sorry!! I cant drive a ", vehicle)


chimp1 = Chimpangee("Chimp", "Cha", "30-04-1982", "Sign") 

chimp1.summary()
chimp1.drive("Car")


def drive(homanoid, vehicle):
    homanoid.drive(vehicle)
    

human2 = Human("Nikhil", "Borhade", "12-08-2005", "Marathi")  
chimp2 = Chimpangee("Chimp", "Cha", "12-08-2005", "Sign") 


drive(human2, "Car")

drive(chimp2, "Car")


#########################################################################

import abc

class Shape(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def area(self):
      pass
  
class Rectangle(Shape):
    
   def __init__(self, x,y):
      self.l = x
      self.b=y
      
   def area(self):
      return self.l*self.b
      
      
r = Rectangle(10,20)
print('area: ', r.area())

class Square(Shape):
    
   def __init__(self, side):
      self.side = side
      
   def area(self):
      return self.side*self.side

s = Square(15)
print('area: ', s.area())


@Shape.register
class Circle():
    
   def __init__(self, radius):
      self.radius = radius
      
   def area(self):
      return ((22/7) * self.radius * self.radius)
      
c = Circle(5)

def get_area(shape):
    print('area: ', shape.area())

get_area(s)
get_area(r)
get_area(c)

l = [Rectangle(10,20), Rectangle(10,10), Rectangle(15,20), Square(10), Square(15), Square(20), Circle(5), Circle(15)]

for shape in l:
    get_area(shape) 

