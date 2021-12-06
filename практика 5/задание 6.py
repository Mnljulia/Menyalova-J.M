# -- coding: utf-8 --
def i():
    x=int(input('n='))
    i=0
    sum=0
    while x!=0:
        sum+=x
        i+=1
        x=int(input('n='))
    print(sum/i)
print(i())