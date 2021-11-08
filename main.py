from file_io import read_data
from rand_generators import SNBRandGenerator, unstandartPuasson, SNB, poisson
from xi_sq import xi_sq

NUM_OF_INTERVALS = 100
SMALL_SEQUENCE_LENGTH = 40
BIG_SEQUENCE_LENGTH = 40

#чтение данных
data = read_data('./data.txt')
h = data['lambda']
sp = [
    (data['s1'], data['p1']),
    (data['s2'], data['p2']),
    (data['s3'], data['p3']),
    ]

sequenceFiles = [
    ('SNB-sequence-40-1.txt', 'SNB-sequence-100-1.txt'),
    ('SNB-sequence-40-2.txt', 'SNB-sequence-100-2.txt'),
    ('SNB-sequence-40-3.txt', 'SNB-sequence-100-3.txt'),
    ]

analisysFiles = [
    ('SNB-analisys-40-1.txt', 'SNB-analisys-100-1.txt'),
    ('SNB-analisys-40-2.txt', 'SNB-analisys-100-2.txt'),
    ('SNB-analisys-40-3.txt', 'SNB-analisys-100-3.txt'),
    ]

for params, sFile, aFile in zip(sp, sequenceFiles, analisysFiles):
    s, p = params
    fileBigSequence, fileSmallSequence = sFile
    fileBigAnalisys, fileSmallAnalisys = aFile

    #генерация последовательностей длиной 40 и 100 на основе биноминального генератора
    SNBSequence = SNB(s, p, range(NUM_OF_INTERVALS))
    smallSequence = SNBRandGenerator(s, p, SMALL_SEQUENCE_LENGTH, NUM_OF_INTERVALS)
    bigSequence = SNBRandGenerator(s, p, BIG_SEQUENCE_LENGTH, NUM_OF_INTERVALS)

    fileSmallSequence = open(fileSmallSequence, 'w')
    fileSmallSequence.write(str(smallSequence))
    fileSmallSequence.close()

    fileBigSequence = open(fileBigSequence, 'w')
    fileBigSequence.write(str(bigSequence))
    fileBigSequence.close()

    #проверка данных на соответствие хи-квадрат гипотезе
    smallResult = xi_sq(smallSequence, SMALL_SEQUENCE_LENGTH, SNBSequence)
    bigResult = xi_sq(bigSequence, BIG_SEQUENCE_LENGTH, SNBSequence)

    fileSmallAnalisys = open(fileSmallAnalisys, 'w')
    fileSmallAnalisys.write('Вычисленная статистика: {}\n'.format(smallResult['calculated']))
    fileSmallAnalisys.write('Достигнутый уровень значимости: {}\n'.format(smallResult['theorethical']))
    fileSmallAnalisys.write('Гипотеза о согласии распределения: {}\n'.format(smallResult['valid']))
    fileSmallAnalisys.close()

    fileBigAnalisys = open(fileBigAnalisys, 'w')
    fileBigAnalisys.write('Вычисленная статистика: {}\n'.format(bigResult['calculated']))
    fileBigAnalisys.write('Достигнутый уровень значимости: {}\n'.format(bigResult['theorethical']))
    fileBigAnalisys.write('Гипотеза о согласии распределения: {}\n'.format(bigResult['valid']))
    fileBigAnalisys.close()


#генерация последовательностей длиной 40 и 100 на основе генератора Пуассона
poissonSequence = poisson(h, range(NUM_OF_INTERVALS))
smallSequence = unstandartPuasson(h, SMALL_SEQUENCE_LENGTH, NUM_OF_INTERVALS)
bigSequence = unstandartPuasson(h, BIG_SEQUENCE_LENGTH, NUM_OF_INTERVALS)

fileSmallSequence = open('poisson-sequence-40.txt', 'w')
fileSmallSequence.write(str(smallSequence))
fileSmallSequence.close()

fileBigSequence = open('poisson-sequence-100.txt', 'w')
fileBigSequence.write(str(bigSequence))
fileBigSequence.close()

#проверка данных на соответствие хи-квадрат гипотезе
smallResult = xi_sq(smallSequence, SMALL_SEQUENCE_LENGTH, poissonSequence)
bigResult = xi_sq(bigSequence, BIG_SEQUENCE_LENGTH, poissonSequence)

fileSmallAnalisys = open('poisson-analisys-40.txt', 'w')
fileSmallAnalisys.write('Вычисленная статистика: {}\n'.format(smallResult['calculated']))
fileSmallAnalisys.write('Достигнутый уровень значимости: {}\n'.format(smallResult['theorethical']))
fileSmallAnalisys.write('Гипотеза о согласии распределения: {}\n'.format(smallResult['valid']))
fileSmallAnalisys.close()

fileBigAnalisys = open('poisson-analisys-100.txt', 'w')
fileBigAnalisys.write('Вычисленная статистика: {}\n'.format(bigResult['calculated']))
fileBigAnalisys.write('Достигнутый уровень значимости: {}\n'.format(bigResult['theorethical']))
fileBigAnalisys.write('Гипотеза о согласии распределения: {}\n'.format(bigResult['valid']))
fileBigAnalisys.close()