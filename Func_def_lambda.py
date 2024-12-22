# Создание и использование функций def и lambda
# Функция - подпрограмма, которая содержит в себе повторяющийся код. В дальнейшем нет необходимости писать полноценный код, а можно обратиться к заранее сформированной функции

# Создание функции
def test_func():
    # Ключевое слово pass - при вызове функции ничего не происходит
    #pass
    print("Hello", end=" ")
    print("World")

test_func()
test_func()
test_func()

# Функция с принимаемым параметром
def test_func2(word):
    # word - параметр
    print(word)
# Вызов функции с передаваемым параметром
test_func2("hi")
test_func2(12345)

# Функции суммы без возврата переменной - аналог void в С/С++
def summ(a, b):
    return print(a + b)

summ(4, 5)
summ("H", "i")
summ(5.6, 7.9)

# Компилятор пишет в warning, что функция ничего не возвращает, хотя есть return
# Связано с тем, что в return вызывается print
res1 = summ(10, 50)

# Функция с возвратом переменной - non void C/C++
def summ2(a, b):
    return a + b

res = summ2(4, 5)
print(res)

# Поиск минимального элемента списка
nums = [4121, 23467, 63343, 46798, 56253]

minimal = nums[0]
for i in nums:
    if i < minimal:
        minimal = i

print(minimal)

nums2 = [12354.4, 1541.1, 15415.0, 3215.7, 12098.7]
minimal2 = nums2[0]
for i in nums2:
    if i < minimal:
        minimal = i

print(minimal2)

# Функция для поиска минимального числа

nums3 = [1124.634, 93451.5, 1046.7, 10956.0, 14667, 7614.7]
def minimal_fin(list_f):
    minimal3 = list_f[0]
    for el in list_f:
        if el < minimal3:
            minimal3 = el
    return minimal3

res3 = minimal_fin(nums3)
res2 = minimal_fin(nums2)
res = minimal_fin(nums)
print("min of all lists: ", res, "  ", res2, "   ", res3)
print("list 3 min = ", minimal_fin(nums3))
print("list 2 min = ", minimal_fin(nums2))
print("list 1 min = ", minimal_fin(nums))

# Анонимные функции - lambda
# Непонятно, для чего их использовать. Функция вроде анонимная, то есть без имени, однако согласно уроку мы сразу записываем ее результат в переменную
func = lambda x, y: x * y
res_l = func(5, 10)
print(func(5, 10))
print(res_l)


