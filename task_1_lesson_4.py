import timeit
"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""

# сложность O(n) - линейная


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [element for element in nums if element % 2 == 0] # было использовано списковое включение сложность также линейная


numbers = [i for i in range(1000)]

print(timeit.timeit("func_1(numbers)", globals=globals(), number=1000))
print(timeit.timeit("func_2(numbers)", globals=globals(), number=1000))

print(timeit.timeit("func_1(numbers)", globals=globals(), number=10000))
print(timeit.timeit("func_2(numbers)", globals=globals(), number=10000))

print(timeit.timeit("func_1(numbers)", globals=globals(), number=100000))
print(timeit.timeit("func_2(numbers)", globals=globals(), number=100000))

"""
0.0759311
0.0361075

0.7631146
0.36765380000000003

7.569732
3.6651717
"""
# время выполнения примерно при помощи спискового включения примерно в 2 раза меньше, что говорит об эффективности данного метода