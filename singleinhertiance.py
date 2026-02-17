class Animal: 
   def speak(self):
     return "Animal speaks"
class Dog(Animal):
   def bark(self):
     return "Dog barks"
dog = Dog()
print(dog.speak()) # Output: Animal speaks
print(dog.bark()) # Output: Dog barks