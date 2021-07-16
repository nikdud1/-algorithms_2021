from collections import defaultdict
from functools import reduce
"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""
def calc():
    numbers = defaultdict(list)
    for i in range(2):
        n = input("Введите 16 число ")
        numbers[i+1] = list(n)
    print(numbers)
    sum_res = sum([int(''.join(i),16) for i in numbers.values()])
    print("Сумма в 16 системе равна ", list('%X' % sum_res))
    mul_res = reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in numbers.values()])
    print("Произведение в 16 системе равна ", list('%X' % mul_res))


class HexOperations:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number
    def __add__(self, other):
        return list(hex(int(''.join(self.first_number),16) + int(''.join(other.second_number),16)))[2:]
    def __mul__(self, other):
        return list(hex(int(''.join(self.first_number),16) * int(''.join(other.second_number),16)))[2:]


calc()

first = list(input("Введите 16 число "))
second = list(input(("Введите 16 число ")))
sum = HexOperations(first, second) + HexOperations(first, second)
mul = HexOperations(first, second) * HexOperations(first, second)
print(sum)
print(mul)