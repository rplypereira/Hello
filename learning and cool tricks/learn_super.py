from typing import Any


class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def info(self):
        l,w = self.length,self.width
        print(f"area={l*w} perimeter={2*(l+w)}")
        
class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
        

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __getattr__(self, key): #__getattribute__ always runs regardless whether obj.smth exists/__getattr__ runs only when we obj.smth and smth is a non-existent attr. however if smth exists, value will be returned as normal
        return key
    
dog = Dog('rocky',5)
print(dog.name)
print(dog.age)
print(dog.test) 
        
a= Rectangle(5,3)
a.info()
b= Square(7)
b.info()