#1035

f1 = input().split()
a = int(f1[0])
b = int(f1[1])
c = int(f1[2])
d = int(f1[2])

if b > c and d > a and (c+d) > (a+b) and c > 0 and d > 0 and a%2==0:
    print(f'Valores aceitos')
else:
    print(f'Valores não aceitos')


#1036

f1 = input().split()
a = float(f1[0])
b = float(f1[1])
c = float(f1[2])

if a==0 or a<0:
    print(f'Impossivel calcular')
else:
    x1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')


#1036

n1 = float(input())

if 0 <= n1 <= 25:
    print(f'Intervalo [0,25]')
if 25 < n1 <= 50:
    print(f'Intervalo (25,50]')
if 50 < n1 <= 75:
    print(f'Intervalo (50,75]')
if 75 < n1 <= 100:
    print(f'Intervalo (75,100]')
if 0 > n1 or 100 < n1:
    print(f'Fora de intervalo')


#1038

lulu = input().split()
a = int(lulu[0])
b = int(lulu[1])

if a==1:
    x1 = float(4.00*b)
    print(f'Total: R$ {x1:.2f}')
if a==2:
    x2 = float(4.50*b)
    print(f'Total: R$ {x2:.2f}')
if a==3:
    x3 = float(5.00*b)
    print(f'Total: R$ {x3:.2f}')
if a==4:
    x4 = float(2.00*b)
    print(f'Total: R$ {x4:.2f}')
if a==5:
    x5 = float(1.50*b)
    print(f'Total: R$ {x5:.2f}')

#2.0 4.0 7.5 8.0
#1040


lulu = input().split()
n1 = float(lulu[0])
n2 = float(lulu[1])
n3 = float(lulu[2])
n4 = float(lulu[3])

m = (n1*2 + n2*3 + n3*4 + n4*1)/10
print(f'Media: {m:.1f}')

if m >= 7.0:
    print(f'Aluno aprovado.')
if m < 5.0:
    print(f'Aluno reprovado.')
if 5.0 <= m <= 6.9:
    print(f'Aluno em exame.')
    x = float(input())
    print(f'Nota do exame: {x:.1f}')
    m2 = (x + m)/2
    if m2 >= 5.0:
        print(f'Aluno aprovado.')
    else:
        print(f'Aluno reprovado.')
    print(f'Media final: {m2:.1f}')
