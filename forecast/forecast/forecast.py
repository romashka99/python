import random
import numpy
import math

import matplotlib.pyplot as plt
import pandas_datareader as pdr
import datetime

a = 0.5

def activateFunction(summ):
    return (1 / (1 + math.exp(-summ * a)))

def derivative(fun):
    return fun * a * (1 - fun * a)


class Neron:
    def __init__(self):
        self.input = []
        self.w = []
        self.y = 0
        self.d = 0

    def summ(self):
        inputN = numpy.array(self.input)
        wN = numpy.array(self.w)
        return numpy.sum(inputN * wN)

hidden = []
output = []

n = 10
count = 1
countHide = 5
mi = 0.5

data = []

aapl = pdr.get_data_yahoo('AAPL', start = datetime.datetime(2018, 1, 1), end = datetime.datetime.now())

data = aapl['Close'].values / 1000
m = int((len(data) - n) * 0.7)

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

print('\n\n\nДо обучения:')
print('Скрытый слой:')
for item in hidden:
   print('Neron\n w = %s \n' % (item.w))
print('Входной слой:')
for item in output:
   print('Neron\n w = %s \n' % (item.w))

k = int(input())

#Обучение
for i in range(k):
    for j in range(m):
        for neron in hidden:
            neron.input = data[j : j + n]
            neron.y = activateFunction(neron.summ())
        for neron in output:
            neron.input = [item.y for item in hidden]
            neron.y = activateFunction(neron.summ())
            ex = data[j + n + 1]
            neron.d = ex - neron.y
        for neron in hidden:
            neron.d = sum([item.w[hidden.index(neron)] * item.d for item in output])
            for el in range(len(neron.w)):
                neron.w[el] += mi * neron.d * derivative(neron.y) * neron.input[el]
        for neron in output:
            for el in range(len(neron.w)):
                neron.w[el] += mi * neron.d * derivative(neron.y) * neron.input[el]

print('После обучения:\n')
print('Скрытый слой:')
for item in hidden:
    print('Neron\n w = %s \n' % (item.w))
print('Входной слой:')
for item in output:
    print('Neron\n w = %s \n' % (item.w))

test = data[m:]
ex = data[m + n:]
y = []
print('\nТестирование:')
for j in range(len(ex)):
    for neron in hidden:
        neron.input = test[j : j + n]
        neron.y = activateFunction(neron.summ())
    for neron in output:
        neron.input = [item.y for item in hidden]
        neron.y = activateFunction(neron.summ())
        y.append(neron.y)

plt.plot(ex, color = 'darkblue')
plt.plot(y, color = 'crimson')
plt.show() 
