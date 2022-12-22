# 1016
d = int(input())
t = d * 2
print(f'{t} minutos')

# 1017
T = int(input())
V = int(input())
Di = (V * T)
Li = (Di/12)
print('{:.3f}'.format(Li))

# 1018
v = int(input())

n100 = int(v/100)
v = v%100

n50 = int(v/50)
v = v%50

n20 = int(v/20)
v = v%20

n10 = int(v/10)
v = v%10

n5 = int(v/5)
v = v%5

n2 = int(v/2)
v = v%2

n1 = v

print(f'{n100} nota(s) de R$ 100')
print(f'{n50} nota(s) de R$ 50')
print(f'{n20} nota(s) de R$ 20')
print(f'{n10} nota(s) de R$ 10')
print(f'{n5} nota(s) de R$ 5')
print(f'{n2} nota(s) de R$ 2')
print(f'{n1} nota(s) de R$ 1')