from random import random
from math import factorial, trunc, exp
    
def C(m, n):
    return factorial(n)/( factorial(m)*factorial(n - m) )

def SNB(x, s, p):
    return C(x, s+x-1) * p**s * (1-p)**x
    
def poisson(x, h):
    return h**x * exp(-h) / factorial(x)

def SNBRandGenerator(s, p, length, quality=100):
    '''
        Функция-генератор, возвращающая последовательность чисел согласно
        стандартному отрицательному биноминальному распредлению
        
        Parameters
        -----
        s: float
            параметр генератора s
        p: float 
            параметр генератора p
        length: int
            длина сгенерированной последовательности
        quality: int
            количество интервалов деления отрезка [0, 1] (по умолчанию =100)
    '''

    P = [SNB(x, s, p) for x in range(quality)]
    out = []
    for i in range(length):
        r = random()
        for ind, elem in enumerate(P):
            r = r - elem
            if r < 0:
                out.append(ind)
                break

    return out

def unstandartPuasson(h, length, quality=100):
    '''
        Функция-генератор, возвращающая последовательность чисел согласно
        нестандартному распредлению Пуассона

        Parameters
        -----
        h: float
            параметр генератора λ
        length: int
            длина сгенерированной последовательности
        quality: int
            количество интервалов деления отрезка [0, 1] (по умолчанию =100)
    '''

    out = []
    E = list(range(quality))
    # P = [poisson(x, h) for x in range(quality)]
    L = trunc(h)
    Q = sum([poisson(x, h) for x in range(L)])

    for i in range(length):
        r = random()
        r0 = r - Q
        if r0 >= 0:
            for elem in E[L:]:
                r0 -= poisson(elem, h)
                if r0 < 0:
                    out.append(elem)
                    break
        else:
            for elem in E[:L-1:-1]:              
                r0 += poisson(elem, h)
                if r0 >= 0:
                    out.append(elem)
                    break
    
    return out
