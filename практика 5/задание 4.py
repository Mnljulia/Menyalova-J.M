# -- coding: utf-8 --

x = int(input('Введите кол-во километров в первый день: '))
y = int(input('Введите кол-во километров в последний день: '))
i = 1
while x <= y:
    x*=1.1
    i+=1

print(i, ' дней понадобится')