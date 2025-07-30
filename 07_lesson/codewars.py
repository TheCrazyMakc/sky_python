class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):  # Вызывается при print(book)
        return f"Книга: {self.title}"

book = Book("Война и мир")
print(book)  # Книга: Война и мир

# CODEWARS №1
# Задача заключается в реализации функции, которая преобразует булево значение (True/False) в его строковое представление.
def boolean_to_string(b):
    return str(b)


# Создайте функцию, которая принимает параметр, представляющий имя, и возвращает сообщение: "Привет, <имя> как у тебя дела сегодня?".
def greet(name):
    return f"Hello, {name} how are you doing today?"


# Ваша задача - подсчитать, сколько чистых страниц вам нужно. Если n < 0 или m < 0, верните 0.
# Пример:
# n= 5, m=5: 25
# n=-5, m=5: 0
def paperwork(n, m):
    if n > 0 and m > 0:
        return n * m
    else:
        return 0
    

# Это ката о умножении заданного числа на восемь, если оно четное, и на девять в противном случае.
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    
# Первое столетие охватывает период с 1 по 100 год включительно, второе столетие - со 101 по 200 год включительно и т.д.
# Задача
# Учитывая год, верните век, в котором он находится.
# Примеры
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 2742 --> 28
def get_century(year):
    return (year + 99) // 100
# или
def get_century(year):
    return (year - 1) // 100 + 1


# В этом простом задании вам дается число, и вы должны сделать его отрицательным. Но, может быть, это число уже отрицательное?
# Примеры
# make_negative(1); # возвращает -1
# make_negative(-5); # возвращает -5
# make_negative(0); # возвращает 0
def make_negative(number):
    if number <= 0:
        return number
    else:
        return number * -1
# или
def make_negative( number ):
    return -number if number>0 else number
# или
def make_negative( number ):
    return -abs(number)


# Напишите программу, которая вычисляет сумму всех чисел от 1 до num (обоих включительно).
def summation(num):
    return num * (num + 1) // 2
# или
def summation(num):
    total = 0
    for i in range(0, num+1):
        total = total + i
    return total


# Напишите функцию findNeedle(), которая принимает массив, полный мусора, но содержащий одну "иголку"
def find_needle(haystack):
    index = 0
    for i in haystack:
        if i == 'needle':
            return f"found the needle at position {index}"
        else:
            index += 1
# или
def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'

# Напишите функцию для преобразования имени в инициалы.
def get_initials(name):
    # Разделяем имя и фамилию
    parts = name.split() # создаем массив из строки
    
    # Получаем первую букву каждого слова
    initial1 = parts[0][0].upper()
    initial2 = parts[1][0].upper()
    
    # Формируем результат
    return f"{initial1}.{initial2}"
# или
def get_initials(name):
    return '.'.join(word[0].upper() for word in name.split())


# Герой направляется в замок, чтобы завершить свою миссию. 
# Однако ему сказали, что замок окружен парой могущественных драконов! 
# для победы над каждым драконом требуется 2 пули, наш герой понятия не имеет, 
# сколько пуль у него должно быть с собой.. Если предположить, 
# что он захватит определенное количество пуль и двинется вперед, 
# чтобы сразиться с другим определенным количеством драконов, выживет ли он?
# Верните true, если да, или false в противном случае :)
def hero(bullets, dragons):
    if dragons * 2 <= bullets:
        return True
    else:
        return False
# или
def hero(bullets, dragons):
    return bullets >= dragons * 2    


# вывести перевернутое слово
def solution(str):
  return str[::-1]


# два числа: если одно четное, а второе нечетное, то тру, иначе фалс
def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0 or flower2 % 2 == 0 and flower1 % 2 != 0:
        return True
    else:
        return False
    

# List comprehension
def digitize(n):
    # Преобразуем число в строку, переворачиваем и преобразуем каждый символ обратно в число
    return [int(digit) for digit in str(n)[::-1]]
# или
    return [int(x) for x in str(n)[::-1]]
#     Проходит по каждой цифре в перевернутой строке
#     Преобразует каждый символ обратно в целое число
#     Собирает результат в список
# Пошаговый пример
# Возьмем число 35231:
#     str(35231) → '35231'
#     '35231'[::-1] → '13253'
#     Преобразование каждого символа:
#         '1' → 1
#         '3' → 3
#         '2' → 2
#         '5' → 5
#         '3' → 3
#     Результат: [1, 3, 2, 5, 3]


# 
