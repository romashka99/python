

def function(x,y):
    return 11 * x * x + 20 * y * y - 9 * x

def functionX(x):
    return 22 * x - 9

def functionY(y):
    return 40 * y

x0 = 5
y0 = 3
h = 0.002
print('{0:10} | {1:10} | {2:10}'.format('x', 'y', 'f(x,y)'))
print('{0:10.4f} | {1:10.4f} | {2:10.4f}'.format(x0, y0, function(x0,y0)))

for i in range(100):
    x0 = x0 - h * functionX(x0)
    y0 = y0 - h * functionY(y0)
    h -= 0.0001
    print('{0:10.4f} | {1:10.4f} | {2:10.4f}'.format(x0, y0, function(x0,y0)))