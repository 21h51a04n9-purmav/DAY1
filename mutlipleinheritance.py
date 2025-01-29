class Bird:
    def fly(self):
        return "This bird can fly."
class Mammal:
    def walk(self):
        return "This mammal can walk."
class Bat(Bird,Mammal):
    def dance(self):
        return "Nattukuthu"
bat=Bat()
print(bat.fly())
print(bat.walk())
print(bat.dance())
print("*****************")
m1=Mammal()
m1=bat
print(m1.dance())

class Women:
    def free(self):
        return "Free bus"
class Men:
    def bike(self):
        return "Can ride bike"
class Person(Women,Men):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender    
    def display(self):
        print(f"{self.name},{self.age},{self.gender}")   
    def read(self):
        return "can read"
person=Person('varshitha',20,'female')
print(person.free())
print(person.bike())   
print(person.read())
print("*****************************************")
p1=Women()
p1=person
print(p1.read())
person.display()