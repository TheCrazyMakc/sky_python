from user import User
from card import Card

alex = User("Alex")

alex.sayName()
alex.sayAge()
alex.setAge(33)
alex.sayAge()

card = Card("1234 4567 7890 0000", "11/28", "Alex F")
card.pay(1000)

alex.addCard(card)
alex.getCard().pay(1000)
