import random
import numpy
import math

def activateFunction(summ):
    return (1 / (1 + math.exp(-summ)))

class Neron:
    def __init__(self):
        self.input = []
        self.w = []
        self.y = 0
        self.d = 0
        self.b = 0

    def summ(self):
        inputN = numpy.array(self.input)
        wN = numpy.array(self.w)
        return numpy.sum(inputN * wN)

data = [[0, 0], [0, 1], [1, 0], [1, 1]]
dataex = [0, 1, 1, 0]
b = [1/2, 3/2, 1/2]

hidden = []
output = []

n = 2
m = 4
count = 1
countHide = 2
mi = 0.2

index = 0
for i in range(countHide):
    neron = Neron()
    for j in range(n):
        w = random.uniform(0, 1)
        neron.w.append(w)
    hidden.append(neron)

for i in range(count):
    neron = Neron()
    for j in range(countHide):
        w = random.uniform(0, 1)
        neron.w.append(w)
    output.append(neron)

print('До обучения:')
print('Скрытый слой:')
for item in hidden:
   print('Neron\n w = %s \n' % (item.w))
print('Входной слой:')
for item in output:
   print('Neron\n w = %s \n' % (item.w))

k = int(input())

for i in range(k):
    for j in range(m):
        for neron in hidden:
            neron.input = data[j]
            neron.y = activateFunction(neron.summ())
        for neron in output:
            neron.input = [item.y for item in hidden]
            neron.y = activateFunction(neron.summ())
            ex = dataex[j]
            neron.d = ex - neron.y
        for neron in hidden:
            neron.d = sum([item.w[hidden.index(neron)] * item.d for item in output])
            for el in range(len(neron.w)):
                neron.w[el] += mi * neron.d * neron.y * (1 - neron.y) * neron.input[el]
        for neron in output:
            for el in range(len(neron.w)):
                neron.w[el] += mi * neron.d * neron.y * (1 - neron.y) * neron.input[el]

print('После обучения:\n')
print('Скрытый слой:')
for item in hidden:
    print('Neron\n w = %s \n' % (item.w))
print('Входной слой:')
for item in output:
    print('Neron\n w = %s \n' % (item.w))

print('\nТестирование:')
count = 4
test = [[0, 0], [0, 1], [1, 0], [1, 1]]
testex = [0, 1, 1, 0]
y = []
countTrue = 0

for j in range(m):
    for neron in hidden:
        neron.input = test[j]
        neron.y = activateFunction(neron.summ())
    for neron in output:
        neron.input = [item.y for item in hidden]
        neron.y = activateFunction(neron.summ())
        y.append(neron.y)
                
for i in range(count):
    if testex[i] == int(y[i]):
        countTrue += 1
print('eq = %.3f' % (countTrue / count))

