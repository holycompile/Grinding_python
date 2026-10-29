class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def show(self):
        print("My name is "+ self.name)

p1=Person("John",30)
p1.show()