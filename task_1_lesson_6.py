from memory_profiler import profile
"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""


# Посчитать четные и нечетные цифры введенного натурального числа.

@profile
def parity_1(number, even=0, odd=0):
    if number == 0:
        return even, odd
    else:
        if number % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
        number = number // 10
        return parity_1(number, even, odd)


# Использование цикла вместо рекурсии
@profile
def parity_2(number, even=0, odd=0):
    while number != 0:
        if (number % 10) % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
        number = number // 10
    return even, odd


@profile
def revers_1(number):
    number2 = int(number) % 10
    rest = int(number) // 10
    if rest == 0:
        return str(number2)
    else:
        return str(number2)+str(revers_1(rest))


@profile
def revers_2(number):
    number = str(number)
    return number[::-1]


@profile
def min_1(lst):
    min_number = lst[0]
    for i in lst:
        for j in lst:
            if i <= j:
                min_number = i
    return min_number


@profile
def min_2(lst):
    min_number = lst[0]
    for i in lst:
        if i < min_number:
            min_number = i
    return min_number


parity_1(1234)
parity_2(1234)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     18.9 MiB     18.9 MiB           1   @profile
    30                                         def parity_1(number, even=0, odd=0):
    31     18.9 MiB      0.0 MiB           1       if number == 0:
    32     18.9 MiB      0.0 MiB           1           return even, odd
    33                                             else:
    34                                                 if number % 2 == 0:
    35                                                     even = even + 1
    36                                                 else:
    37                                                     odd = odd + 1
    38                                                 number = number // 10
    39                                                 return parity_1(number, even, odd)




Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     18.9 MiB     18.9 MiB           2   @profile
    30                                         def parity_1(number, even=0, odd=0):
    31     18.9 MiB      0.0 MiB           2       if number == 0:
    32     18.9 MiB      0.0 MiB           1           return even, odd
    33                                             else:
    34     18.9 MiB      0.0 MiB           1           if number % 2 == 0:
    35                                                     even = even + 1
    36                                                 else:
    37     18.9 MiB      0.0 MiB           1               odd = odd + 1
    38     18.9 MiB      0.0 MiB           1           number = number // 10
    39     18.9 MiB      0.0 MiB           1           return parity_1(number, even, odd)




Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     18.9 MiB     18.9 MiB           3   @profile
    30                                         def parity_1(number, even=0, odd=0):
    31     18.9 MiB      0.0 MiB           3       if number == 0:
    32     18.9 MiB      0.0 MiB           1           return even, odd
    33                                             else:
    34     18.9 MiB      0.0 MiB           2           if number % 2 == 0:
    35     18.9 MiB      0.0 MiB           1               even = even + 1
    36                                                 else:
    37     18.9 MiB      0.0 MiB           1               odd = odd + 1
    38     18.9 MiB      0.0 MiB           2           number = number // 10
    39     18.9 MiB      0.0 MiB           2           return parity_1(number, even, odd)




Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     18.9 MiB     18.9 MiB           4   @profile
    30                                         def parity_1(number, even=0, odd=0):
    31     18.9 MiB      0.0 MiB           4       if number == 0:
    32     18.9 MiB      0.0 MiB           1           return even, odd
    33                                             else:
    34     18.9 MiB      0.0 MiB           3           if number % 2 == 0:
    35     18.9 MiB      0.0 MiB           1               even = even + 1
    36                                                 else:
    37     18.9 MiB      0.0 MiB           2               odd = odd + 1
    38     18.9 MiB      0.0 MiB           3           number = number // 10
    39     18.9 MiB      0.0 MiB           3           return parity_1(number, even, odd)




Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     18.9 MiB     18.9 MiB           5   @profile
    30                                         def parity_1(number, even=0, odd=0):
    31     18.9 MiB      0.0 MiB           5       if number == 0:
    32     18.9 MiB      0.0 MiB           1           return even, odd
    33                                             else:
    34     18.9 MiB      0.0 MiB           4           if number % 2 == 0:
    35     18.9 MiB      0.0 MiB           2               even = even + 1
    36                                                 else:
    37     18.9 MiB      0.0 MiB           2               odd = odd + 1
    38     18.9 MiB      0.0 MiB           4           number = number // 10
    39     18.9 MiB      0.0 MiB           4           return parity_1(number, even, odd)




Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    43     18.9 MiB     18.9 MiB           1   @profile
    44                                         def parity_2(number, even=0, odd=0):
    45     18.9 MiB      0.0 MiB           5       while number != 0:
    46     18.9 MiB      0.0 MiB           4           if (number % 10) % 2 == 0:
    47     18.9 MiB      0.0 MiB           2               even = even + 1
    48                                                 else:
    49     18.9 MiB      0.0 MiB           2               odd = odd + 1
    50     18.9 MiB      0.0 MiB           4           number = number // 10
    51     18.9 MiB      0.0 MiB           1       return even, odd

Таким образом при использовании рекурсии Profile сработал 4 раза, а при использовании цикла 1 раз. 
Использование функции с циклом намного эффективнее, так как не используется стек 
И алгоритм с циклом требует в 4 раза меньше памяти
"""

revers_1(123)
revers_2(123)


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     19.0 MiB     19.0 MiB           1   @profile
    55                                         def revers_1(number):
    56     19.0 MiB      0.0 MiB           1       number2 = int(number) % 10
    57     19.0 MiB      0.0 MiB           1       rest = int(number) // 10
    58     19.0 MiB      0.0 MiB           1       if rest==0:
    59     19.0 MiB      0.0 MiB           1           return str(number2)
    60                                             else:
    61                                                 return str(number2)+str(revers_1(rest))




Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     19.0 MiB     19.0 MiB           2   @profile
    55                                         def revers_1(number):
    56     19.0 MiB      0.0 MiB           2       number2 = int(number) % 10
    57     19.0 MiB      0.0 MiB           2       rest = int(number) // 10
    58     19.0 MiB      0.0 MiB           2       if rest==0:
    59     19.0 MiB      0.0 MiB           1           return str(number2)
    60                                             else:
    61     19.0 MiB      0.0 MiB           1           return str(number2)+str(revers_1(rest))




Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     19.0 MiB     19.0 MiB           3   @profile
    55                                         def revers_1(number):
    56     19.0 MiB      0.0 MiB           3       number2 = int(number) % 10
    57     19.0 MiB      0.0 MiB           3       rest = int(number) // 10
    58     19.0 MiB      0.0 MiB           3       if rest==0:
    59     19.0 MiB      0.0 MiB           1           return str(number2)
    60                                             else:
    61     19.0 MiB      0.0 MiB           2           return str(number2)+str(revers_1(rest))




Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    64     19.0 MiB     19.0 MiB           1   @profile
    65                                         def revers_2(number):
    66     19.0 MiB      0.0 MiB           1       number = str(number)
    67     19.0 MiB      0.0 MiB           1       return number[::-1]
    
Таким образом при использовании рекурсии Profile сработал 3 раза, а при использовании среза 1 раз. 
Использование функции со срезом намного эффективнее, так как не используется стек 
И алгоритм с циклом требует в 3 раза меньше памяти
"""

print(min_1([4, 3, 2, 1]))
print(min_2([4, 3, 2, 1]))

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    69     19.2 MiB     19.2 MiB           1   @profile
    70                                         def min_1(lst):
    71     19.2 MiB      0.0 MiB           1       min_number = lst[0]
    72     19.2 MiB      0.0 MiB           5       for i in lst:
    73     19.2 MiB      0.0 MiB          20           for j in lst:
    74     19.2 MiB      0.0 MiB          16               if i <= j:
    75     19.2 MiB      0.0 MiB          10                   min_number = i
    76     19.2 MiB      0.0 MiB           1       return min_number


1


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    80     19.2 MiB     19.2 MiB           1   @profile
    81                                         def min_2(lst):
    82     19.2 MiB      0.0 MiB           1       min_number = lst[0]
    83     19.2 MiB      0.0 MiB           5       for i in lst:
    84     19.2 MiB      0.0 MiB           4           if i < min_number:
    85     19.2 MiB      0.0 MiB           3               min_number = i
    86     19.2 MiB      0.0 MiB           1       return min_number


1
"""
