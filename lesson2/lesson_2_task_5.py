def month_to_season(month):  # Добавлен параметр
    if not 1 <= month <= 12:
        return "Номер месяца должен быть от 1 до 12"
    elif month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    else:
        return "Осень"

month = int(input("Введите номер месяца: "))
result = month_to_season(month)
print(result)
