from timeit import timeit
"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000

Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""

# O(n^2)


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

# O(n * log( log n))


def eratosthenes(n):     # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу

    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve



i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
i = int(input('Введите верхнюю границу для Решето Эратосфена: ')) # В решето задается не индекс, а верхняя граница, далее формируется список, в котором непростые числа равны 0
print(eratosthenes(i))

print(timeit("simple(10)", globals=globals(), number=10))
print(timeit("(eratosthenes(29))", globals=globals(), number=10))

print(timeit("simple(100)", globals=globals(), number=10))
print(timeit("(eratosthenes(541))", globals=globals(), number=10))

print(timeit("simple(1000)", globals=globals(), number=10))
print(timeit("(eratosthenes(7919))", globals=globals(), number=10))

"""
0.00013139999999989271
4.550000000058674e-05

0.014507100000000328
0.0006650999999990859

2.9876825
0.010185299999999842

Таким образом чем больше простое число, которое мы пытаемся найти, тем эффективнее справляется алгоритм Эратосфена
"""

