import math

def square(num):
  if num <= 0:
    print("ошибка ввода. введите положительное число")    
  else:
    return print(math.ceil(num ** 2)) # округление вверх

num = float(input("введите положительное число: "))

square(num)
