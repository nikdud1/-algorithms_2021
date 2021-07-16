from collections import deque
from timeit import timeit
"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""


def lst_init(lst_1):
    for i in range(1000):
        lst_1.append(i)


def deque_init(deque_1):
    for i in range(1000):
        deque_1.append(i)


def lst_append_left(lst):
    lst.insert(0, 10)
    return lst


def lst_pop_left(lst):
    lst.pop(0)
    return lst


def lst_extend_left(lst_1, lst_2):
    n = 0
    for i in range(len(lst_2)-1, -1, -1):
        lst_1.insert(lst_2[i], n)
        n = n + 1
    return lst_1


def append_left(deque_1):
    deque_1.appendleft(10)
    return deque_1


def pop_left(deque_1):
    deque_1.popleft
    return deque_1


def extend_left(deque_1, deque_2):
    deque_1.extendleft(deque_2)
    return deque_1


lst = []
deque_1 = deque()
print(timeit("lst_init(lst)", globals=globals(), number=10000))
print(timeit("deque_init(deque_1)", globals=globals(), number=10000))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
deque_1 = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

lst_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
deque_2 = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

print(timeit("lst_append_left(lst)", globals=globals(), number=10000))
print(timeit("append_left(deque_1)", globals=globals(), number=10000))

print(timeit("lst_pop_left(lst)", globals=globals(), number=10000))
print(timeit("pop_left(deque_1)", globals=globals(), number=10000))

print(timeit("lst_extend_left(lst, lst_2)", globals=globals(), number=10000))
print(timeit("extend_left(deque_1, deque_2)", globals=globals(), number=10000))


"""
0.5990419
0.49811970000000005

0.03588839999999993
0.0011586000000001206

0.010961100000000057
0.001133099999999887

11.054502300000001
0.0030535000000000423

Если заполнение списка происходит с конца, то скорость примерно одинаковая, так как сложность одинаковая O(n)
В остальных случаях дек работает намного быстрее, так как в случае списка сложность становиться линейной, а дек O(n)
Уникальные Функции дека намного быстрее, а общие функции имеют примерно одинаковую скорость
"""
