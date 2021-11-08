from random import random
from math import factorial, trunc, exp
    
def C(m, n):
    return factorial(n)/( factorial(m)*factorial(n - m) )

def SNB(s, p, sequence):
    return [C(k, s+k-1) * p**s * (1-p)**k for k in sequence]
    
def poisson(h, sequence):
    return [h**k * exp(-h) / factorial(k) for k in sequence]

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

    P = SNB(s, p, range(quality))
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

    E = list(range(quality))
    P = poisson(h, E)
    out = []
    L = trunc(h)
    Q = sum(P[:L])

    for i in range(length):
        r = random()
        r0 = r - Q
        if r0 >= 0:
            for ind, elem in enumerate(P[L:]):
                r0 = r0 - elem
                if r0 < 0:
                    out.append(E[ind + L])
                    break
        else:
            for ind, elem in enumerate(P[:L-1:-1]):              
                r0 = r0 + elem
                if r0 >= 0:
                    out.append(E[L - ind - 1])
                    break
    
    return out
