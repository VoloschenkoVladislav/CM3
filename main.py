from file_io import read_data
from rand_generators import SNBRandGenerator, unstandartPuasson, SNB, poisson
from xi_sq import xi_sq

NUM_OF_INTERVALS = 100
SMALL_SEQUENCE_LENGTH = 40
BIG_SEQUENCE_LENGTH = 100
WORK_DIR = './results/'

def writeSequence(fileName, sequence):
    f = open(WORK_DIR + fileName, 'w')
    f.write(str(sequence))
    f.close()

def writeAnalisys(fileName, analysis):
    f = open(WORK_DIR + fileName, 'w')
    f.write('Calculated statistics: {}\n'.format(analysis['calculated']))
    f.write('The achieved level of significance: {}\n'.format(analysis['theorethical']))
    f.write('The hypothesis of the agreement of the distribution: {}\n'.format(analysis['valid']))
    f.close()

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

    writeSequence(fileSmallSequence, smallSequence)
    writeSequence(fileBigSequence, bigSequence)

    #проверка данных на соответствие хи-квадрат гипотезе
    smallResult = xi_sq(smallSequence, SMALL_SEQUENCE_LENGTH, SNBSequence)
    bigResult = xi_sq(bigSequence, BIG_SEQUENCE_LENGTH, SNBSequence)

    writeAnalisys(fileSmallAnalisys, smallResult)
    writeAnalisys(fileBigAnalisys, bigResult)

fileSmallSequence, fileBigSequence, fileSmallAnalisys, fileBigAnalisys = (
                                                                          'poisson-sequence-40.txt',
                                                                          'poisson-sequence-100.txt',
                                                                          'poisson-analisys-40.txt',
                                                                          'poisson-analisys-100.txt',
                                                                         )

#генерация последовательностей длиной 40 и 100 на основе генератора Пуассона
poissonSequence = poisson(h, range(NUM_OF_INTERVALS))
smallSequence = unstandartPuasson(h, SMALL_SEQUENCE_LENGTH, NUM_OF_INTERVALS)
bigSequence = unstandartPuasson(h, BIG_SEQUENCE_LENGTH, NUM_OF_INTERVALS)

writeSequence(fileSmallSequence, smallSequence)
writeSequence(fileBigSequence, bigSequence)

#проверка данных на соответствие хи-квадрат гипотезе
smallResult = xi_sq(smallSequence, SMALL_SEQUENCE_LENGTH, poissonSequence)
bigResult = xi_sq(bigSequence, BIG_SEQUENCE_LENGTH, poissonSequence)

writeAnalisys(fileSmallAnalisys, smallResult)
writeAnalisys(fileBigAnalisys, bigResult)
