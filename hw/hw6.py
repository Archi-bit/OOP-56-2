"""Библиотека Faker используется для генерации фейковых данных (например имен, адресов, номер телефонов, фамилии и тд).
Faker может быть полезна при тестировании программ, когда нужно много случайных, но реалистичных данных.
Например, можно использовать Faker, чтобы заполнить базу данных "пробными" пользователясми
"""

# импортируем faker
from faker import Faker

fake = Faker()

print("name:", fake.name())
print("address:",fake.address())
print("phone number:",fake.phone_number())
print("company:",fake.company())
print("email:",fake.email())