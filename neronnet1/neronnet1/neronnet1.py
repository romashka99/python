import random
import numpy

class Neron:
    def __init__(self, i):
        self.input = []
        self.w = []
        self.y = 0
        self.ex = 0
        self.w0 = random.uniform(0, 1)
        self.e = 0
        self.i = i

    def summ(self):
        inputN = numpy.array(self.input)
        wN = numpy.array(self.w)
        return numpy.sum(inputN * wN)

dataex = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]]

nerons = []

n = 36
m = 16
ncount = 4
mi = 0.2

for i in range(ncount):
    neron = Neron(i)
    for j in range(n):
        w = random.uniform(0, 1)
        neron.w.append(w)
    nerons.append(neron)
            
print('До обучения:')
for item in nerons:
   print('Neron %d \n w = %s \n w0 = %f \n' % (item.i, item.w, item.w0))

data = []
dataX = []

with open('Data.txt', 'r') as file:
    data = file.readlines()  

for line in data:
    dataX.append([int(elem) for elem in line.strip()])

k = int(input())

for i in range(k):
    serr = 0
    for item in nerons:
        for j in range(m):
            item.input = dataX[j]
            item.ex = dataex[nerons.index(item)][j]
            if item.summ() > item.w0:
                item.y = 1
            else:
                item.y = 0
            item.e = item.y - item.ex
            serr = serr + item.e**2
            for el in range(n):
                item.w[el] -= mi * item.e * item.input[el]
            item.w0 += mi * item.e
    print('Ошибка = %f' % serr)

print('\nПосле обучения:')
for item in nerons:
   print('Neron %d \n w = %s \n w0 = %f' % (item.i, item.w, item.w0))

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

for item in nerons:
    for element in testX:
        item.input = element
        if item.summ() > item.w0:
            index = testX.index(element)
            print(testX.index(element))
            y.insert(index, '')
            print("sum = %f w0 = %f" % (item.summ(), item.w0))
            if (item.i == 0):
                print('%s - это +' % (element))
                y.insert(index, '+')
            if (item.i == 1):
                print('%s - это -' % (element))
                y.insert(index, '-')
            if (item.i == 2):
                print('%s - это *' % (element))
                y.insert(index, '*')
            if (item.i == 3):
                print('%s - это /' % (element))
                y.insert(index, '/')
                
for i in range(count):
    if ex[i] == y[i]:
        countTrue += 1

print('eq = %.3f' % (countTrue / count))