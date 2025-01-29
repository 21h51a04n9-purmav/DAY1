class Cat:
    def sound(self):
        print("cat is making sound as Meow")
class Dog:
    def sound(self):
        print("dog is Barking")
for animal in [Cat(),Dog()]:
    animal.sound()

class Person:
    def greet(self):
        print("Hello")
class Person2:
    def greet(self):
        print("Good morning")
for man in [Person(),Person2()]:
    man.greet()
 
