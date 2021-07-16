from collections import OrderedDict
from timeit import timeit
"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


def dict_init(dict_1):
    for i in range(1000):
        dict_1[i] = i
    return dict_1


def ord_dict_init(ord_dict_1):
    for i in range(1000):
        ord_dict_1[i] = i
    return ord_dict_1


def dict_values(dict_1):
    return dict_1.values()


def ord_dict_values(ord_dict_1):
    return ord_dict_1.values()


dict_2 = dict()
ord_dict_2 = OrderedDict()
print(timeit("dict_init(dict_2)", globals=globals(), number=10000))
print(timeit("ord_dict_init(ord_dict_2)", globals=globals(), number=10000))

dict_2 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
ord_dict_2 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

print(timeit("dict_values(dict_2)", globals=globals(), number=10000))
print(timeit("ord_dict_values(ord_dict_2)", globals=globals(), number=10000))

"""
0.5354423
0.8178228999999999
0.001248300000000091
0.0012553999999997956
"""


# Таким образом, нет смысла использовать OrderedDict в Python 3.6 и более поздних версиях, так как некоторые действия он выполняет дольше ем словарь и имеет почти такой же функционал
