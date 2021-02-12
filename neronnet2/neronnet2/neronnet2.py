import random
import numpy
import math

def activateFunction(summ):
    return (1 / (1 + math.exp(-summ)))

def derivative(fun):
    return fun * (1 - fun)


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


dataex = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]]

hidden = []
output = []

n = 36
m = 16
count = 4
countHide = 16
mi = 0.5

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

data = []
dataX = []

with open('Data.txt', 'r') as file:
    data = file.readlines()  

for line in data:
    dataX.append([int(elem) for elem in line.strip()])

k = int(input())

for i in range(k):
    for j in range(m):
        for neron in hidden:
            neron.input = dataX[j]
            neron.y = activateFunction(neron.summ())
        for neron in output:
            neron.input = [item.y for item in hidden]
            neron.y = activateFunction(neron.summ())
            ex = dataex[output.index(neron)][j]
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

testX = []

with open('Test.txt', 'r') as file:
    data = file.readlines()

for line in data:
    testX.append([int(elem) for elem in line.strip()])

print('\nТестирование:')
count = 16
ex = ['+', '+', '+', '+', '-', '-', '-', '-', '*', '*', '*', '*', '/', '/', '/', '/']
y = []
countTrue = 0

for j in range(m):
    yn = []
    for neron in hidden:
        neron.input = testX[j]
        neron.y = activateFunction(neron.summ())
    for neron in output:
        neron.input = [item.y for item in hidden]
        neron.y = activateFunction(neron.summ())
        yn.append(neron.y)
    index = yn.index(max(yn))
    operation = ''
    if index == 0:
        operation = '+'
    if index == 1:
        operation = '-'
    if index == 2:
        operation = '*'
    if index == 3:
        operation = '/'
    y.append(operation)
                
for i in range(count):
    if ex[i] == y[i]:
        countTrue += 1
print('eq = %.3f' % (countTrue / count))