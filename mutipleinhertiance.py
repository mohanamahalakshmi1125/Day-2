class Flyer:
  def fly(self):
   return "Can fly"
class Swimmer:
  def swim(self):
    return "Can swim"
class Duck(Flyer, Swimmer):
  def quack(self):
    return "Duck quacks"
duck = Duck()
print(duck.fly()) # Output: Can fly
print(duck.swim()) # Output: Can swim
print(duck.quack()) # Output: Duck quack