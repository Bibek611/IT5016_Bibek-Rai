# Define a 'Person' class
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def greet (self):
        print(f"Hello, My Name is {self.name} and I am {self.age} years old.")

person1=Person("James", 29)
person1.greet()


#Task2: Define a 'Rectangle' class with methods for area and Perimeter
class Rectangle ():
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2*(self.width+self.height)
    
rect=Rectangle(4, 5)
print(f"Area: {rect.area()}")  # Output Area of rectangle is 20
print(f"Perimeter: {rect.perimeter()}")  # Output Perimeter of rectangle is 18


#Task3
class Car:
    def __init__(self, color, model, year):
        self.color=color
        self.model=model
        self.year=year

    def drive (self):
        print(f"The {self.color} {self.model} {self.year} is driving.")

    def stop (self):
        print(f"The {self.color} {self.model} {self.year} has stopped.")

    def carinfo(self):
        print(f"Car Info:{self.year} {self.color} {self.model} ")


car1=Car("Black", "Tesla", "2011")
car2=Car("Blue", "Maruti", "2008")

car1.drive()
car1.stop()
car1.carinfo()



