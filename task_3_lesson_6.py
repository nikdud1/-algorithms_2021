from memory_profiler import memory_usage
"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""


def parity_1(number, even=0, odd=0):
    print("Использованная память во время рекурсии: ", memory_usage())
    if number == 0:
        return even, odd
    else:
        if number % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
        number = number // 10
        return parity_1(number, even, odd)


print("Использованная память до рекурсии: ", memory_usage())
parity_1(12345678923)
