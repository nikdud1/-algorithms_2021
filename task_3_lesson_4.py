from timeit import timeit
from random import randint
from cProfile import run
"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""

# рекурсия


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)

# цикл while


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

# срез


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

# цикл for


def revers_4(enter_num):
    enter_num = str(enter_num)
    s = ""
    for i in range(len(enter_num) - 1, -1, -1):
        s = s + enter_num[i]
    return int(s)


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Рекурсия')
print(timeit("revers_1(num_100)", globals=globals(), number=100000))
print(timeit("revers_1(num_1000)", globals=globals(), number=100000))
print(timeit("revers_1(num_10000)", globals=globals(), number=100000))


print('Цикл while')
print(timeit("revers_2(num_100)", globals=globals(), number=100000))
print(timeit("revers_2(num_1000)", globals=globals(), number=100000))
print(timeit("revers_2(num_10000)", globals=globals(), number=100000))

print('Срез')
print(timeit("revers_3(num_100)", globals=globals(), number=100000))
print(timeit("revers_3(num_1000)", globals=globals(), number=100000))
print(timeit("revers_3(num_10000)", globals=globals(), number=100000))

print('цикл for')
print(timeit("revers_4(num_100)", globals=globals(), number=100000))
print(timeit("revers_4(num_1000)", globals=globals(), number=100000))
print(timeit("revers_4(num_10000)", globals=globals(), number=100000))




