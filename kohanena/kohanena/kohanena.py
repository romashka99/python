import random
import numpy
import math
import array

class Neron:
    def __init__(self):
        self.input = []
        self.w = []
        self.r = 0
        self.name = ""
        self.count = 0

    def evklid(self):
        inputN = numpy.array(self.input)
        wN = numpy.array(self.w)
        return numpy.sum((inputN - wN) ** 2)


kohanena = []

n = 4
count = 3
mi = 0.5

with open('data.txt', 'r') as file:
    data = file.readlines()

m = len(data)

dataX = []
dataName = []

for line in data:
    line = line.strip().split('\t')
    dataX.append([float(elem) for elem in line[:n]])
    dataName.append(line[n])

for i in range(len(dataX)):
    for j in range(len(dataX[i])):
        dataX[i][j] = dataX[i][j] / 10

#n = 2
#count = 4
#dataX = [[0.8, 0.8], [0.8, 0.1], [0.2, 0.8], [0.1, 0.2]]
#dataName = ['Пожилой человек с высоким доходом', 'Пожилой человек с низким доходом', 'Молодой человек с высоким доходом', 'Молодой человек с низким доходом']
#m = len(dataX)

#n = 4
#count = 3
#dataX = [[0.51, 0.35, 0.14, 0.02], [0.7, 0.32, 0.47, 0.14], [0.58, 0.27, 0.51, 0.19]]
#dataName = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
#m = len(dataX)

for i in range(count):
    neron = Neron()
    for j in range(n):
        w = 0
        if j == 0:
            w = random.uniform(0.8, 1)
        if j == 1:
            w = random.uniform(0.5, 0.8)
        if j == 2:
            w = random.uniform(0.3, 0.5)
        if j == 3:
            w = random.uniform(0, 0.3)
        neron.w.append(w)
    kohanena.append(neron)

print('До обучения:')
print('Слой кохонена:')
for item in kohanena:
   print('Neron\n w = %s \n' % (item.w))

k = int(input())
#Обучение
for i in range(k):
    for neron in kohanena:
        neron.count = 0
    for j in range(m):
        indexData = random.randint(0, m - 1)
        r = []
        for neron in kohanena:
            neron.input = dataX[indexData]
            neron.r = neron.evklid()
            r.append(neron.r)
        index = r.index(min(r))
        kohanena[index].name = dataName[indexData]
        kohanena[index].count += 1
        for el in range(len(kohanena[index].w)):
            kohanena[index].w[el] -= mi * (kohanena[index].w[el] - kohanena[index].input[el])


print('После обучения:')
for item in kohanena:
   print('Neron\n w = %s \n' % (item.w))
print('Слой кохонена:')
for item in kohanena:
   print('Neron %d кластер = %s количество = %d \n' % (kohanena.index(item), item.name, item.count))


