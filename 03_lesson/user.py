class User():

  def __init__(self, first_name, last_name):
    print("запись создана")
    self.first_name = first_name
    self.last_name = last_name
    # self.fullName = first_name + " " + last_name

  def sayFirstName(self):
    print("меня зовут", self.first_name)

  def sayLastName(self):
    print("моя фамилия", self.last_name)

  def setFullName(self):
    print(f"{self.first_name} {self.last_name}")
