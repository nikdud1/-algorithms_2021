import hashlib

"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
list = []
example_str = "papa"
for i in range (len(example_str)):
    for j in range(i+1, len(example_str) + 1):
        if example_str[i:j] != example_str and(hashlib.sha256(example_str[i:j].encode()).hexdigest() not in list):
            list.append(hashlib.sha256(example_str[i:j].encode()).hexdigest())
            print(example_str[i:j])
print(len(list))
