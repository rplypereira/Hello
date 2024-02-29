#width =10
#precision = 4
#number = 12.34567
#print(f"result: {number:{width}.{precision}}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name}."
    
person = Person("Alice",30)
print(f"{person.greet()} I am {person.age} years old.")