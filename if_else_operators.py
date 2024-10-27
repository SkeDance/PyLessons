# Проверка данных от пользователя
from Variables import number

user_data = int(input("Enter a number: "))
if user_data != 5:
    print("ready to start")
    if user_data > 5:
        print("Number greater than 5")
    else:
        print("Number less than 5")


# Проверка булевых переменных
isHappy = True
if  isHappy:
    print("Happy")
elif not isHappy:
    print("Sad")
# Проверка нескольких условий
if isHappy and user_data > 5:
    print("Happy x2")
elif isHappy and user_data < 5:
    print("Sad x1")

# Тернарный оператор
data = input()
number = 5 if data == "Five" else 0