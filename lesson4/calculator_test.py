import pytest
from calculator import Calculator

calculator = Calculator()

@pytest.mark.parametrize( 'num1, num2, result', [ 
  (4,5,9), 
  (-6, -10, -16), 
  (-6, 6, 0), 
  (5.61, 4.29, 9.9), 
  (10, 0, 10) 
  ])
def test_sum_positive_nums(num1, num2, result):
  calculator = Calculator()
  res = calculator.sum(num1, num2)
  assert res == result

@pytest.mark.parametrize( 'nums, result', [ 
  ([], 0), 
  ([1,2,3,4,5,6,7,8,9,5], 5) 
  ])
def test_avg_list(nums, result):
  calculator = Calculator()
  res = calculator.avg(nums)
  assert res == result

def test_sum_positive_nums():
  calculator = Calculator()
  res = calculator.sum(4, 5)
  assert res == 9


def test_sum_negative_nums():
  calculator = Calculator()
  res = calculator.sum(-6, -10)
  assert res == -16

def test_sum_flout_nums():
  calculator = Calculator()
  res = calculator.sum(5.6, 4.3)
  res = round(res, 1)
  assert res == 9.9

def test_sum_zero_nums():
  calculator = Calculator()
  res = calculator.sum(10, 0)
  assert res == 10

def test_div_positive():
  calculator = Calculator()
  res = calculator.div(10, 2)
  assert res == 5

def test_div_by_zero():
  calculator = Calculator()
  with pytest.raises(ArithmeticError):  # тут указываем на наличие ошибка, чтобы тест прошел
    calculator.div(10, 0)

def test_avg_positive():
  calculator = Calculator()
  numbers = [1,2,3,4,5,6,7,8,9,5]
  res = calculator.avg(numbers)
  assert res == 5

# pytest -k "sum"  # Запуск тестов, содержащих 'sum' в названии

# + +
# - - 
# - +
# . .
# n 0

# print("start")
# res = calculator.sum(4, 5)
# assert res == 9

# res = calculator.sum(-6, -10)
# assert res == -16 

# res = calculator.sum(-6, 6)
# assert res == 0

# res = calculator.sum(5.6, 4.3)
# res = round(res, 1)
# assert res == 9.9

# res = calculator.sum(10, 0)
# assert res == 10

# # деление
# res = calculator.div(10, 2)
# assert res == 5

# res = calculator.div(10, 0)
# assert res == None

# numbers = []
# res = calculator.avg(numbers)
# assert res == 0

# numbers = [1,2,3,4,5,6,7,8,9,5]
# res = calculator.avg(numbers)
# assert res == 5

print("finish")

