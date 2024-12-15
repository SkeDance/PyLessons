# Словари в Python
# Словарь позволяет обращаться к элементу списка или кортежа при помощи определенного ключа
# [] - список
# () - кортеж
# {} - словарь
from email.header import USASCII
from itertools import count

# 4 является ключом к элементу 3
country = {4: 3}
# При обращении к элементу 3 мы указываем ключ 4
print(country[4])

# Обращение через кортеж
country = {(4, 3): 3}
# при обращении к элементу 3 мы указываем кортеж в качестве ключа (4, 3)
print(country[(4, 3)])

# Обращение через bool
country = {True: 3}
# при обращении к элементу 3 мы указываем ключ True
print(country[True])

# Словари удобны для описания объектов
country = {'code': 'RU', "name": "Russia", 'population': 144}
# Для обращения к элементу словаря нам не нужно знать его индекс, а только ключ
print(country['name'], country['population'])

# Альтернативное создание словаря
country = dict(code = 'RU', name = "Russia", population = 144)
print(country['name'], country['population'])

# Функция .items()
print("use items():", country.items())

# Перебор словаря в цикле
for key, value in country.items():
    print(key, " - ", value)

# Другие функции словарей
print(country.get("code"))
# Удаление определенного элемента по ключу
country.pop('code')
print("use pop('code'):", country)

country = dict(code = 'RU', name = "Russia", population = 144)

# Получение только ключей словаря
print("use keys():", country.keys())
# Получение только значений словаря
print("use values():", country.values())
# Удаление последнего элемента словаря
country.popitem()
print("use popitem() first time:", country)
country.popitem()
print("use popitem() second time:", country)

# Обновление значений словаря
country.update()
country['code'] = 'None'
print("update dict:", country)


# Очистка словаря
country.clear()
print("use clear():", country)

# Применение словаря внутри другого словаря
person = {
    'user_1': {
        'first_name': 'SkyDance',
        'second_name': 'Aleinikov',
        'age': 23,
        'city': ['Moscow', 'str.Kurako', 34],
        'grades': {'math': 5, 'science': 5, 'economics': 4}
    },
    'user_2': {
        'first_name': 'Ilya',
        'second_name': 'Refraction',
        'age': 22,
        'city': ['Moscow', 'str.Transportnaya', 152],
        'grades': {'math': 5, 'science': 4, 'economics': 5}
    }
}

print(person['user_1']['city'][1])
print(person['user_1']['city'])
print(person['user_1'])

