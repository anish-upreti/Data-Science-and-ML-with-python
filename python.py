class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I’m {self.name} and I’m {self.age} years old.")

p1 = Person("Diana", 25)
p1.greet()
