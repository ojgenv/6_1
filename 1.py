""" 
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) | """

x = int(input('Введите число '))
y = 0

while x > 0:
    y += x % 10
    x = x // 10
print(y)