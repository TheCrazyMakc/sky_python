from mailing import Mailing
from address import Address

# Создаем адреса
sender_address = Address(
    index="123456",
    city="Москва",
    street="Ленина",
    house="10",
    apartment="5"
)

recipient_address = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Пушкина",
    house="20",
    apartment="15"
)

# Создаем почтовое отправление
mailing = Mailing(
    to_address=recipient_address,
    from_address=sender_address,
    cost=500,
    track="123456789012"
)

# Можно вывести данные для проверки
print(f"Трек-номер: {mailing.track}")
print(f"Стоимость: {mailing.cost}")
print(f"Отправитель: {mailing.from_address.city}, {mailing.from_address.street} {mailing.from_address.house}")
print(f"Получатель: {mailing.to_address.city}, {mailing.to_address.street} {mailing.to_address.house}")
