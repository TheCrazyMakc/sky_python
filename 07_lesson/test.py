# # def summation(num):
# #     total = 0
# #     for i in range(0, num+1):
# #         total = total + i
# #         print(total)
# #     return total

# # summation(8)

# # def test(num):
# #     total = 0
# #     for i in range(0, 10):
# #         print(f'это значение {i}')
# #         total = total + i
# #         # print(f'это значение {total}')
# #     return total

# # test(8)

# # def get_initials(name):
# #     # Разделяем имя и фамилию
# #     parts = name.split()
# #     print(parts)
# #     # Получаем первую букву каждого слова
# #     initial1 = parts[0][0].upper()
# #     print(initial1)
# #     initial2 = parts[1][0].upper()
# #     print(initial2)
# #     # Формируем результат
# #     return f"{initial1}.{initial2}"

# # get_initials('lost again')

# # n = 54321

# # def digitize(n):
# #     mass = str(n)
# #     print(mass)
# #     mass2 = mass[::-1]
# #     print(mass2)
# #     answer = mass.split()
# #     print(answer)
# #     return answer

# # digitize(n)

# # ______________________________________________________________________________________

# class House():
#   '''описание дома'''
#   def __init__(self, street, number):
#     '''свойство дома'''
#     self.street = street
#     self.number = number
#     self.age = 0

#   def build(self):
#     '''строит дом'''
#     print('Дом на улице ' + self.street + ' под номером ' + str(self.number) + ' построен.')

#   def age_of_house(self, year):
#     '''возраст дома'''
#     self.age += year

# house1 = House("Московская", 20)
# house2 = House("Московская", 21)

# house1.build()
# print(house1.street)
# print(house2.number)
# print(house1.age)

# house1.age_of_house(5)
# print(house1.age)

# class ProspectHouse(House):
#   '''дома на проспекте'''
#   def __init__(self, prospect, number):
#     super().__init__(prospect, number)
#     self.prospect = prospect

# PrHouse = ProspectHouse("Ленина", 5)
# print(PrHouse.prospect)
# print(PrHouse.number)

# # _______________________________________________________________________________________

