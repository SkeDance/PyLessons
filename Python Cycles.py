# Циклы в Python
# Hard wrap file -> settings ->  editor -> general -> appearance -> show hard wrap
# Цикл - это конструкция, позволяющая выполнять определенный фрагмент кода несколько раз подряд. Количество выполнений мы можем указывать самостоятельно
# В ЯП Python существует два цикла - for и while

# in range(6) - задаёт количество повторений кода в цикле - 6 раз
# in range(1, 6) - выполняет код для с 1 по 6 не включительно
# in range(1, 6, 2) - 2 указывает шаг цикла
# for i in range(6):
#     print(i)

# Через цикл for можно перебирать строки, так как любая строка это список, состоящий из определённого количества элементов
word = "Hello world"
count = 0
for i in word:
    if i == "l":
        count += 1

print(count)

# Помимо цикла for в ЯП Python существует такой цикл как while
# Разница между циклом for и while заключается лишь в формате записи

x = 5
while x < 15:
    print(x)
    x += 1

isHasCar = True

while isHasCar:
    if input("Enter data ") == "stop":
        isHasCar = False
        break

# Операторы в циклах
# break - обеспечивает вынужденный выход из цикла при заданном условии

# Прекращает цикл при x == 5
#     if x == 5:
#         break

# continue - обеспечивает пропуск итерации цикла

# Пропускает все четные значения x
#     if x % 2 == 0:
#         continue

for x in range(1, 11):

    if x == 5:
        break
    if x % 2 == 0:
        continue
    print(x)

# Нахождение определённого символа в строке
str_inp = input()
found = None
for i in str_inp:
    if i == "а":
        found = True
        break
    else:
        found = False
print(found)
