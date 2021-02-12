import random

def function(x):
    return -6 * x * x + 120 * x + 9000

def mutation(item):
    item1 = list(item[2:])
    k1 = random.randint(0, len(item1) - 1)
    item1[k1] = str(abs(int(item1[k1]) - 1))
    return '0b' + ''.join(item1)


def crossing(a, b):
    k1 = random.randint(0, len(a) - 1)
    a1 = a[2:]
    b1 = b[2:]
    print('{0:5} - {1:5}'.format(a1, a1[k1:] + b1[:k1]))
    return '0b' + a1[k1:] + b1[:k1]

def crossingover(a, b):
    child1 = crossing(a,b)
    child2 = crossing(b,a)
    print()
    if function(int(child1,2)) >= function(int(child2,2)):
        return child1
    else:
        return child2


class Individ:
    def __init__(self, x):
        self.x = x
        self.value = bin(x)
        self.y = function(x)
        self.count = 0
        self.f = 0
        self.random = 0
        self.rcount = 0

print('Введите количество поколений:')
n = int(input())

print('Введите количество особей:')
k = int(input())

print('Введите количество особей с мутацией:')
m = int(input())

F = 0
parents = []
cross = []

for i in range(k):
    parents.append(Individ(random.randint(0, 31)))
    F += parents[i - 1].y

maxY = 0
maxX = 0

for i in range(n):
    print()
    print('Поколение %d' % (i + 1))
    print('Родительский состав:')
    print('{0:10} | {1:15} | {2:10} | {3:20} | {4:20} | {5:10} | {6:25}'.format('Значение x', 'Двоичный код', 'F(x)', 'F(X)/sum(F(X))=pi', 'Количество копий', 'Рандом', 'Реальное количество копий'))
    for item in parents:
        item.f = item.y / F
        item.count = item.f * k
        item.random = random.uniform(0, 1)
        item.rcount = int(item.count // 1)
        if item.random < (item.count % 1):
            item.rcount += 1
        for i in range(item.rcount):
            cross.append(item.value)
        print('{0:10d} | {1:15} | {2:10.2f} | {3:20.2f} | {4:20.2f} | {5:10.2f} | {6:25d}'.format(item.x, item.value, item.y, item.f, item.count, item.random, item.rcount))
    print()    
    print('Состав для скрещивания:')
    print(cross)
    print()
    print('Cкрещивание:')
    childrens = []

    for item in range(k):
        p1 = random.randint(0, len(cross) - 1)
        p2 = random.randint(0, len(cross) - 1)
        childrens.append(crossingover(cross[p1], cross[p2]))

    print('Мутация:')
    print('{0:5} | {1:5}'.format('До', 'После'))
    for item in range(m):
        k1 = random.randint(0, len(childrens) - 1)
        child = childrens[k1]
        childrens[k1] = mutation(childrens[k1])
        print('{0:5} | {1:5}'.format(child, childrens[k1]))
    
    print()
    parents = []
    F = 0
    print('Cостав детей:')
    print('{0:10} | {1:15} | {2:15}'.format('Значение x', 'Двоичный код', 'F(x)'))
    for i in range(k):
        parents.append(Individ(int(childrens[i - 1], 2)))
        F += parents[i - 1].y
        print('{0:10d} | {1:15} | {2:15.2f}'.format(parents[i - 1].x, parents[i - 1].value, parents[i - 1].y))
    fun = [item.y for item in parents]
    x = [item.x for item in parents]
    max1 = max(fun)
    i = fun.index(max1)
    print('max: x = %d f(x) = %d ' % (x[i], max1))
    if maxY < max1:
        maxY = max1
        maxX = x[i]

print('max: x = %d f(x) = %d ' % (maxX, maxY))