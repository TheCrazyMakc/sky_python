class User:
  age = 0

  def __init__(self, name): # конструктор
    print("я создался")
    self.username = name

  def sayName(self):
    print("меня зовут", self.username)

  def sayAge(self):
    print("мой возраст", self.age)

  def setAge(self, newAge):
    self.age = newAge

  def addCard(self, card):
    self.card = card

  def getCard(self):
    return self.card