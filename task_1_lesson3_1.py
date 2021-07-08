from time import time
"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
def list_append(lst, number):
    start = time()
    for i in range(number):
        lst.insert(i,0) # сложность О(N)
    end = time()
    print("list takes", (end-start) * 10000)
def dict_append(dct,number):
    start = time()
    for i in range(number):
        dct[i] = i  # сложность О(1)
    end = time()
    print("dictionary takes ",(end-start) * 10000)
def comparison(lst, number, dict ):
    for i in range(number):
        lst.insert(i, 0)  # сложность О(N)
    for i in range(number):
        dict[i] = i  # сложность О(1)
    start = time() * 10000
    del lst[2]  # O(N)
    end = time() * 10000
    print("list takes ", (end - start) * 10000)
    start = time() * 10000
    del dict[2]  # O(1)
    end = time() * 10000
    print("dictionary takes ", (end - start) * 10000) # словарь быстрее, так сложность меньше
example_list = []
example_dictionary = {}
list_append(example_list, 100000)
dict_append(example_dictionary,100000) # словарь быстрее заполняется
comparison(example_list, 100000, example_dictionary)
