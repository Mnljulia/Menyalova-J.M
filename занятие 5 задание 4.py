# -- coding: utf-8 --
x = int(input('Введите число:\n'))
y = int(input('Введите число:\n'))
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)