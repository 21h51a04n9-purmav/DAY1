class Employee:
    def __init__(self,name,age,position):
        self.name=name
        self.age=age
        self.position=position
    def display(self):
        print(f"Name:{self.name},Age:{self.age},position:{self.position}")
emp1=Employee("varshitha",20,"Manager")
emp2=Employee("jyothi",23,"HR")
emp3=Employee("vinuthna",24,"senior manager")
employee=[emp1,emp2,emp3]
for i in employee:
    i.display()
