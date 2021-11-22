import math
import scipy.integrate as integrate
import tools
import file_io

def xi_sq(x, n, p):
    '''
        Функция для проверки гипотезы по критерию хи-квадрат
        
        --------------
        
        Параметры:
        * x - последовательность случайных чисел
        * n - количество чисел в последовательности
        * p - последовательность теоретических вероятностей некоторой случайной величины с дискретным распределением
    
    
        --------------
        
        Возвращает словарь с тремя элементами, имеющими ключи calculated, theorethical, valid
    '''

    alpha = 0.05
    intervals = list(range(len(p)))
    nin = [0]*len(p)
    countIntervals = [0]*len(p)
    
    for i, _ in enumerate(intervals):
        countIntervals[i] = x.count(i) 
        nin[i] = countIntervals[i] / n
        
    tools.drawHist(intervals, nin)
    
    sChi = 0
    for i in range(len(p)):
        sChi += ((nin[i] - p[i])**2)/p[i]
    sChi *= n
    print("S* = "+str(sChi))
    r = len(p) - 1
    pSchi = 1/(2**(r/2)*math.gamma(r/2))
    pSchi1, _ = integrate.quad(lambda xx: xx**(r/2 - 1)*math.exp(-xx/2), sChi, 1000)
    pSchi = pSchi*pSchi1
    
    rez = {}
    
    rez["calculated"] = round(pSchi, 4)
    rez["theorethical"] = alpha
    if pSchi > alpha:
        rez["valid"] = True
    else:
        rez["valid"] = False
    
    
    return rez
