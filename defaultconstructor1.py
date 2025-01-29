class DefaultConstructor:
    def __init__(self):
        self.message="Defaultconstructor"
    def display(self):
        print(self.message)
obj=DefaultConstructor()
obj.display()