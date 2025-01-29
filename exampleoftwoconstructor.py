class Example:
    def __init__(self,name):
        print(f"First constructor:Hello {name}")
    def __init__(self,age):
        print(f"Second constructor:Age is {age}")
obj=Example(20)
class Example:
    def __init__(self,*args):
        if len(args)==1:
            print(f"Hello {args[0]}")
        elif len(args)==2:
            print(f"Hello {args[0]}, you are {args[1]} years old.")
        else:
            print(f"Hello {args[0]}, you are {args[1]} years old,you are from {args[2]}.")
obj=Example("varshitha",20,"Hyderabad")

class Example:
    def __init__(self,studentname,**kwargs):
        self.studentname=studentname
        if "name" in kwargs and "age" in kwargs:
            print(f"Hello {kwargs['name']},you are {kwargs['age']} yearsold.")
        elif "name" in kwargs:
            print(f"Hello {kwargs['name']}")
        self.xfeild=kwargs['name']
obj=Example("jyo",age=21)
