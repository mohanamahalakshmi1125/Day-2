class Animal:
    def speak(self):
       return "Animal speaks"
class Dog(Animal):
    def bark(self):
       return "Dog barks"
class Cat(Animal):
    def meow(self):
       return "Cat meows"
dog = Dog()
cat = Cat()
print(dog.speak()) # Output: Animal speaks
print(cat.speak()) # Output: Animal speaks
print(dog.bark()) # Output: Dog barks
print(cat.meow()) # Output: Cat meows
