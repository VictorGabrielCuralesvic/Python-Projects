import math
# 1015.1
p1 = input().split()
x1 = float(p1[0])
y1 = float(p1[1])

p2 = input().split()
x2 = float(p2[0])
y2 = float(p2[1])

d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print('{:.4f}'.format(d))

# 1015.2

l1 = input().split()
z1 = float(l1[0])
w1 = float(l1[1])

l2 = input().split()
z2 = float(l2[0])
w2 = float(l2[1])

D = math.sqrt((z2-z1)**2 + (w2-w1)**2)

print('{:.4f}'.format(D))