x1,y1 = input().split()
x2,y2 = input().split()

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

distancia = ((x2-x1)**2 + (y2-y1)**2) **(1/2)

print('{:.4f}'.format(distancia))

