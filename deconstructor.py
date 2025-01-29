class DeconstructorExample:
    def __init__(self):
        self.name="Python"
        print("Object  is created.")
    def __del__(self):
        print("Object is destroyed.")
obj=DeconstructorExample()
del obj

