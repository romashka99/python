import copy
class Point:
    def __init__(self, name, x, y, cl):
        self.name = name
        self.x = x
        self.y = y
        self.cl = cl
        
    def __eq__(self, other): 
        if not isinstance(other, Point):
            return NotImplemented

        return self.name == other.name and self.x == other.x and self.y == other.y and self.cl == other.cl

class PointDes:
    def __init__(self, pointM, point):
        self.pointM = pointM
        self.point = point
        self.d = ((pointM.x - point.x)**2) + ((pointM.y - point.y)**2)

def clone(data):
    clone = []
    for item in data:
        clone.append(copy.deepcopy(item))
    return clone


data = []

with open('Data.txt', 'r') as file:
    data = file.readlines()
points = []
for item in data:
    dataPoint = item.split(' ')
    points.append(Point(dataPoint[0], float(dataPoint[1]),  float(dataPoint[2]),  int(dataPoint[3])))


data = []

with open('M.txt', 'r') as file:
    data = file.readlines()
pointsM = []
for item in data:
    dataPoint = item.split(' ')
    pointsM.append(Point(dataPoint[0], float(dataPoint[1]),  float(dataPoint[2]),  int(dataPoint[3])))

points1 = []
start = 1
while start == 1:
    for item in pointsM:
        print('%s(%.2f, %.2f)' % (item.name, item.x, item.y))
    if points == points1:
        start = 0
    else:
        points1 = clone(points)
        e = 0
        for item in points:
            table = []
            for itemM in pointsM:
                table.append(PointDes(itemM, item))
            des = [item.d for item in table]
            e += min(des)**2
            item.cl = table[des.index(min(des))].pointM.cl
            format = '%s|' % item.name
            for d in des:
                format += ' %7.2f |' % d
            format += ' %d ' % item.cl
            print(format)
        for itemM in pointsM:
            x = 0
            y = 0
            count = 0
            for itemP in points:
                if itemP.cl == itemM.cl:
                    x += itemP.x
                    y += itemP.y
                    count = count + 1
            itemM.x = x / count
            itemM.y = y /count
        print('Сумма квадратов ошибок = %7.3f' % e)

