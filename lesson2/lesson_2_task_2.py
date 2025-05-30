def is_year_leap(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"год {year} = True")
  else:
    print(f"год {year} = False")

year = int(input("Введите год: "))

is_year_leap(year)