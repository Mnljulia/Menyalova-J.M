# -*- coding: utf-8 -*-

def i():
    n = 1
    i = 0
    l = 0
    while True:
        x = int(input("Введите число - "))
        if x == 0:
            break
        if(l != 0):
    
            if(x == p):
                n += 1
            else:
                if(i < n):
                    i = n
                n = 1
        p = x
        l+=1
    print(max(i, n))

i()