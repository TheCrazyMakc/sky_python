def square(num):
  if num <= 0:
    print("ошибка ввода. введите положительное число")    
  else:
    return print(num ** 2)

num = int(input("введите положительное число: "))

square(num)
