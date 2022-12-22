a = input().split()
c1 = int(a[0])
n1 = int(a[1])
v1 = float(a[2])
t1 = (n1 * v1)

b = input().split()
c2 = int(b[0])
n2 = int(b[1])
v2 = float(b[2])
t2 = (n2 * v2)

tt = (t1 + t2)
print(f'VALOR A PAGAR = U$ {tt:.2f}')