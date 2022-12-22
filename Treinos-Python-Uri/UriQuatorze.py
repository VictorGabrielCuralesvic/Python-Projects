# 1013
lulu = input().split()
a = int(lulu[0])
b = int(lulu[1])
c = int(lulu[2])
m = max(a,b,c)
print(f'{m} eh o maior')

# 1014
d = int(input())
l = float(input())
consumo = (d/l)
print('{:.3f} km/l'.format(consumo))

# 1015
lulu1 = input().split()
x1 = float(lulu1[0])
y1 = float(lulu1[1])

lulu2 = input().split()
x2 = float(lulu2[0])
y2 = float(lulu2[1])

D = ((x2-x1)**2 + (y2-y1)*2)**1/2

print('{:.4f}'.format(D))