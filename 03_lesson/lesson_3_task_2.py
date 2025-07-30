from smartphone import Smartphone

catalog = [] # Создаем пустой каталог

# Заполняем каталог пятью разными смартфонами
catalog.append(Smartphone("Apple", "iPhone 13", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79345678901"))
catalog.append(Smartphone("Huawei", "P40", "+79456789012"))
catalog.append(Smartphone("Google", "Pixel 6", "+79567890123"))


for phone in catalog: # Выводим каталог
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
