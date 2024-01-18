#Mastering Python advanced OOP concepts
#MAGIC METHODS
#__method__

class Example:
    def __new__(cls):
        print("Creating instance")
        return super(Example,cls).__new__(cls)
    
    def __init__(self):
        print("initialising instance")
        

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}, aged {self.age}"
    
    def __repr__(self):
        return f"Person('{self.name}',{self.age})"
        
        
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def __eq__(self,other):
        return self.title == other.title and self.author == other.author       

if __name__ =="__main__":
    #usage
    ex = Example()
    #OUTPUT: Creating Instance, initialising instance
    
    #usage
    p = Person('Alice',30)
    setattr(p,'weight',65) # used to set a new attribute to an object
    print(str(p)) #O/P: Alice, aged 30
    print(repr(p)) #O/P: Person('Alice',30)
    print(p.weight)
    p.weight = 80
    print(p.weight)
    
    b1 = Book("1984","George Orwell")
    b2 = Book("The Fellowship of the ring","J.R.R Tolkien")
    print(b1 == b2) #O/P: False         (__eq__,__ne__,__lt__,__le__,__gt__,__ge__)