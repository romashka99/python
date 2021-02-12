
class Point:
    def __init__(self, name, x, y, cl):
        self.name = name
        self.x = x
        self.y = y
        self.cl = cl

class PointDes:
    def __init__(self, pointM, point, cl):
        self.pointM = pointM
        self.point = point
        self.d = ((pointM.x - point.x)**2) + ((pointM.y - point.y)**2)
        self.cl = cl


data = []

with open('Data.txt', 'r') as file:
    data = file.readlines()
points = []
for item in data:
    dataPoint = item.split(' ')
    points.append(Point(dataPoint[0], int(dataPoint[1]),  int(dataPoint[2]),  int(dataPoint[3])))


data = []

with open('M.txt', 'r') as file:
    data = file.readlines()
pointsM = []
for item in data:
    dataPoint = item.split(' ')
    pointsM.append(Point(dataPoint[0], int(dataPoint[1]),  int(dataPoint[2]),  int(dataPoint[3])))

for itemM in pointsM:
    table = []
    for item in points:
        table.append(PointDes(itemM, item, 0))
    table.sort(key=lambda x: x.d)
    classes = [item.point.cl for item in table]
    for i in range(len(classes)):
        array = classes[:(i+1)]
        table[i].cl = max(array, key = array.count)
    classes = [item.cl for item in table]
    itemM.cl = max(classes, key = classes.count);
    for item in table:
         print('%s | %7.2f | %d | %d' % (item.point.name, item.d, item.point.cl, item.cl))
    print('Точка %s принадлежит классу %d' % (itemM.name, itemM.cl))