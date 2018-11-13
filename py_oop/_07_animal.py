# class definition (blueprint)
class Animal():

  # class constructor method
  def __init__(self, name):

    # instance properties
    self.name = name
    self.food = None
    
    print ("종류는 {} ".format(name))

  def eat(self, food ):
    self.food = food
    print ("{}가 {} 을 먹다".format(self.name, self.food))
  def poop(self):
    print ("{}가 똥을 누다".format(self.name))

# class definition, inherits from Animal
class Dog(Animal):

  # class constructor method
  def __init__(self,breed):
    # property
    self.breed = breed
    if self.breed == True:
        print("새끼를 낳다")
    else: print("새끼가 없다")
   

    # super call, calls the super constructor
    Animal.__init__(self, "강아지")

# Cat extends Animal
class Cat(Animal):

  def __init__(self, name, color):
    self.color = color
    Animal.__init__(self, name)


