#1041

vi = input().split()
x = float(vi[0])
y = float(vi[1])

if x > 0:
    if y > 0:
        print(f'Q1')
    if y < 0:
        print(f'Q4')
if x < 0:
    if y > 0:
        print(f'Q2')
    if y < 0:
        print(f'Q3')
if x == 0:
    if y != 0:
        print(f'Eixo Y')
    if y == 0:
        print(f'Origem')
if x != 0:
    if y == 0:
        print(f'Eixo X')

#1041.2

l = input().split()
x = float(l[0])
y = float(l[1])

if x == 0:
    if y == 0:
        print(f'Origem')
    if y!= 0:
        print(f'Eixo Y')
if y == 0:
    if x != 0:
        print(f'Eixo X')
if x > 0:
    if y > 0:
        print(f'Q1')
    if y < 0:
        print(f'Q4')
if x < 0:
    if y > 0:
        print(f'Q2')
    if y < 0:
        print(f'Q3')

#1035

vi = input().split()
a = int(vi[0])
b = int(vi[1])
c = int(vi[2])
d = int(vi[3])
if b > c and d > a and (c+d) > (a+b) and c > 0 and d > 0 and a%2==0:
    print(f'Valores aceitos')
else:
    print(f'Valores nao aceitos')


#1036

vi = input().split()
a = float(vi[0])
b = float(vi[1])
c = float(vi[2])
if a == 0 or (b**2 - 4*a*c) < 0:
    print(f'Impossivel calcular')
else:
    x1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')


#1037

n = float(input())
if 0 <= n <= 25:
    print(f'Intervalo [0,25]')
if 25 < n <= 50:
    print(f'Intervalo (25,50]')
if 50 < n <= 75:
    print(f'Intervalo (50,75]')
if 75 < n <= 100:
    print(f'Intervalo (75,100]')
if 0 > n or 100 < n:
    print(f'Fora do intervalo')


#1038

vi = input().split()
a = int(vi[0])
b = int(vi[1])

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


#1040

vi = input().split()
n1 = float(vi[0])
n2 = float(vi[1])
n3 = float(vi[2])
n4 = float(vi[3])

m = (n1*2 + n2*3 + n3*4 + n4*1)/10
print(f'Media: {m:.1f}')

if m >= 7.0:
    print(f'Aluno aprovado.')
if m < 5.0:
    print(f'Aluno reprovado.')
if 5 <= m <= 6.9:
    print(f'Aluno em exame.')
    ne = float(input())
    print(f'Nota do exame: {ne:.1f}')
    mf = (m+ne)/2
    if mf >= 5.0:
        print(f'Aluno aprovado.')
    else:
        print(f'Aluno reprovado.')
    print(f'Media final: {mf:.1f}')


#1042.1

vi = input().split()
a = int(vi[0])
b = int(vi[1])
c = int(vi[2])

for v in sorted(vi):
    print(f'{v}')
print(f'')
for v in vi:
    print(f'{v}')


#1042.2

vi = list(map(int,input().split()))
a = (vi[0])
b = (vi[1])
c = (vi[2])

for v in sorted(vi):
    print(f'{v}')
print(f'')
for v in vi:
    print(f'{v}')


#1043

vi = list(map(float,input().split()))
a = (vi[0])
b = (vi[1])
c = (vi[2])

if (a+b) > c and (a+c) > b and (c+b) > a:
    p = (a+b+c)
    print(f'Perimetro = {p:.1f}')
else:
    area = (a+b)*c/2
    print(f'Area = {area:.1f}')


#1142
#neste desafio, foi preciso um acumulador para conseguir resolve-lo

n = int(input())
c = 1
for vi in range(1,n+1):
    print(f'{c} {c+1} {c+2} PUM')
    c += 4


#1153
#outro desafio que precisou de um acumulador

n = int(input())
c = 1
for vi in range(0,n):
    c *= (n-vi)
print(f'{c}')


#1155

S = 0
for vi in range(1,101):
    S = (S + 1/vi)
print(f'{S:.2f}')


#1087


while (1):
    vi = input().split()
    x1 = int(vi[0])
    y1 = int(vi[1])
    x2 = int(vi[2])
    y2 = int(vi[3])

    if (x1==0 and x2==0 and y1==0 and y2==0):
        break
    elif (x1==x2) and (y1==y2):
        print(f'0')
    elif (x1==x2) or (y1==y2):
        print(f'1')
    elif abs(x1-x2) == abs(y1-y2):
        print(f'1')
    else:
        print(f'2')


#1095


I = 1
for vi in range(60, -1, -5):
    print(f'I={I} J={vi}')
    I = I + 3


#1097

for vi in range(1,10,2):
    for vi2 in range(vi+6, vi+3, -1):
        print(f'I={vi} J={vi2}')


#1098 (DUVIDA)


i = 0
j = 1
while i <= 2:
    print(f'I={i} J={j}')
    j += 1
    if j == i+4:
        i = (round(i+0.2, 1))
        j = (round(j-2.8, 1))


#1099

n = int(input())
for vi in range(n):
    l = list(map(int,input().split()))
    x = min(l)
    y = max(l)
    s = 0

    for vi2 in range(x+1,y):
        if vi2%2 == 1:
            s += vi2
    print(f'{s}')


#1151

n = int(input())
p = 0
s = 1
print(f'{p}', end=' ')
print(f'{s}', end=' ')
c = 3
while c <= n:
    t = p + s
    print(f'{t}', end=' ')
    p = s
    s = t
    c = c + 1


#1172


X = []
for vi in range(10):
    x = int(input())
    if x <= 0:
        x = 1
    else:
        x = x
    print(f'X[{vi}] = {x}')

#1173

X = []
for vi in range(10):
    if vi == 0:
        x = int(input())

        X.insert(vi,x)
    else:
        x *= 2
        X.insert(vi,x)
    print(f'N[{vi}] = {x}')


#1175

Y = []
for vi in range(20):
    y = int(input())
    Y.insert(vi,y)

for vi in range(20):
    print(f'N[{vi}] = {Y[19-vi]}')

#1175.2 (teste)

Y = []
for vi in range(20):
    y = int(input())
    Y.append(y)
Y.reverse()
for vi in range(20):
    print(f'N[{vi}] = {Y}')


#1176


F = []
p = 0
s = 1
F.append(p)
F.append(s)
for vi in range(60):
    t = p + s
    p = s
    s = t
    F.append(t)
nt = int(input())
for vi in range(nt):
    teste = int(input())
    print(f'Fib({teste}) = {F[teste]}')

#1178


N = []
n = float(input())
for vi in range(100):
    N.insert(vi,n)
    print(f'N[{vi}] = {n:.4f}')
    n /= 2


#1557 (DUVIDA)


m = list()

while True:
    n = int(input())

    if n == 0:
        break


#1044


vi = input().split()
a = int(vi[0])
b = int(vi[1])

if (a%b==0) or (b%a==0):
    print(f'Sao Multiplos')
else:
    print(f'Nao sao Multiplos')


#1045


vlr = list(map(float,input().split()))
A, B, C = sorted(vlr, reverse=True)

continuar = True

if A >= B+C:
    print(f'NAO FORMA TRIANGULO')
    continuar = False
if A**2 == (B**2) + (C**2) and continuar:
    print(f'TRIANGULO RETANGULO')
if A**2 > (B**2) + (C**2) and continuar:
    print(f'TRIANGULO OBTUSANGULO')
if A**2 < (B**2) + (C**2) and continuar:
    print(f'TRIANGULO ACUTANGULO')
if A==B==C and continuar:
    print(f'TRIANGULO EQUILATERO')
if (A==B or B==C) and not (A==B and B==C) and continuar:
    print(f'TRIANGULO ISOSCELES')


#1046


inicio, fim = map(int,input().split())

if inicio<fim:
    tempo = (fim-inicio)
    print(f'O JOGO DUROU {tempo} HORA(S)')
elif inicio>fim:
    tempo = (fim-inicio) + 24
    print(f'O JOGO DUROU {tempo} HORA(S)')
elif inicio==fim:
    tempo = (fim-inicio) + 24
    print(f'O JOGO DUROU {tempo} HORA(S)')


#1047


hi, mi, hf, mf = map(int,input().split())

print(f'{hi}, {mi}, {hf}, {mf}')

if hi<hf and mi<mf:
    t1 = (hf-hi)
    mi = mi+(hi*60)
    mf = mf+(hf*60)
    t2 = (mf-mi)%60
    print(f'O JOGO DUROU {t1} HORA(S) E {t2} MINUTO(S)')
elif hi>hf and mi>mf:
    t1 = (hf-hi)+24
    mi = mi+(hi*60)
    mf = mf+(hf*60)
    t2 = (mf-mi)%60
    print(f'O JOGO DUROU {t1} HORA(S) E {t2} MINUTO(S)')
elif hi==hf and mi==mf:
    t1 = (hf-hi)+24
    mi = mi+(hi*60)
    mf = mf+(hf*60)
    t2 = (mf-mi)%60
    print(f'O JOGO DUROU {t1} HORA(S) E {t2} MINUTO(S)')



hi, mi, hf, mf = map(int,input().split())

mi = mi+(hi*60)
mf = mf+(hf*60)

tempo = mf-mi
if tempo <= 0:
    tempo = (tempo+24)*60

ht = tempo//60
mt = tempo%60

print(f'O JOGO DUROU {ht} HORA(S) E {mt} MINUTO(S)')


#1048


x = float(input())

if x <= 400.00:
    s = x*(15/100)
    r = s+x
    p = 15
    print(f'Novo salario: {r:.2f}\nReajuste ganho: {s:.2f}\nEm percentual: {p} %')
elif 400.01 <=x<= 800.00:
    s = x*(12/100)
    r = s+x
    p = 12
    print(f'Novo salario: {r:.2f}\nReajuste ganho: {s:.2f}\nEm percentual: {p} %')
elif 800.01 <=x<= 1200.00:
    s = x*(10/100)
    r = s+x
    p = 10
    print(f'Novo salario: {r:.2f}\nReajuste ganho: {s:.2f}\nEm percentual: {p} %')
elif 1200.01 <=x<= 2000.00:
    s = x*(7/100)
    r = s+x
    p = 7
    print(f'Novo salario: {r:.2f}\nReajuste ganho: {s:.2f}\nEm percentual: {p} %')
elif x > 2000.00:
    s = x*(4/100)
    r = s+x
    p = 4
    print(f'Novo salario: {r:.2f}\nReajuste ganho: {s:.2f}\nEm percentual: {p} %')


#1049


x = input()
y = input()
z = input()

if x=='vertebrado' and y=='ave' and z=='carnivoro':
    print(f'aguia')
elif x=='vertebrado' and y=='ave' and z=='onivoro':
    print(f'pomba')
elif x=='vertebrado' and y=='mamifero' and z=='onivoro':
    print(f'homem')
elif x=='vertebrado' and y=='mamifero' and z=='herbivoro':
    print(f'vaca')
elif x=='invertebrado' and y=='inseto' and z=='hematofago':
    print(f'pulga')
elif x=='invertebrado' and y=='inseto' and z=='herbivoro':
    print(f'lagarta')
elif x=='invertebrado' and y=='anelideo' and z=='hematofago':
    print(f'sanguessuga')
elif x=='invertebrado' and y=='anelideo' and z=='onivoro':
    print(f'minhoca')


#1050

n = int(input())

if n==61:
    print(f'Brasilia')
elif n==71:
    print(f'Salvador')
elif n==11:
    print(f'Sao Paulo')
elif n==21:
    print(f'Rio de Janeiro')
elif n==32:
    print(f'Juiz de Fora')
elif n==19:
    print(f'Campinas')
elif n==27:
    print(f'Vitoria')
elif n==31:
    print(f'Belo Horizonte')
else:
    print(f'DDD nao cadastrado')


#1051

s = float(input())

if 0<s<=2000.00:
    print(f'Isento')
if 2000.00<s<= 3000.00:
    s8 = s - 2000.00
    i = s8*(8/100)
    print(f'R$ {i:.2f}')
if 3000.00<s<= 4500.00:
    i8 = (8/100)*(1000.00)
    s18 = s - 3000.00
    i = s18*(18/100) + i8
    print(f'R$ {i:.2f}')
elif s>4500.00:
    i8 = (8/100)*(1000.00)
    i18 = (18/100)*(1500.00)
    s28 = s - 4500.00
    i = s28*(28/100) + i8 + i18

    print(f'R$ {i:.2f}')



#1052.1


nm = int(input())
m = ['','January','February','March','April','May','June','July','August','September','October','November','December']
print(f'{m[nm]}')


#1052.2

nm = int(input())

if nm == 1:
    print(f'January')
if nm == 2:
    print(f'February')
if nm == 3:
    print(f'March')
if nm == 4:
    print(f'April')
if nm == 5:
    print(f'May')
if nm == 6:
    print(f'June')


#1059


for vi in range(1,101):
    if vi%2==0:
        print(f'{vi}')


#1060


c = 0
for vi in range(1,7):
    v = float(input())
    if v>0:
        c += 1
print(f'{c} valores positivos')


#1061


d1 = int(input().split()[1])
h1 = input().split(' ')
x = int(h1[0])
y = int(h1[2])
z = int(h1[4])

d2 = int(input().split()[1])
h2 = input().split(' ')
x1 = int(h2[0])
y1 = int(h2[2])
z1 = int(h2[4])

dia = d2 - d1
if (dia <= 0):
    dia = 0

hora = x1 - x
if (hora < 0):
    hora += 24
    dia -= 1

minuto = y1 - y
if (minuto < 0):
    minuto += 60
    hora -= 1

segundos = z1 - z
if (segundos < 0):
    segundos += 60
    minuto -= 1

print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{minuto} minuto(s)')
print(f'{segundos} segundo(s)')


#1064


c = 0
m = 0.0
for vi in range(1,7):
    n = float(input())
    if n > 0:
        c += 1
        m += n
print(f'{c} valores positivos')
print(f'{m/c:.1f}')


#1065


c = 0
for vi in range(1,6):
    n = int(input())
    if n%2==0:
        c += 1
print(f'{c} valores pares')


#1066

p = 0
i = 0
po = 0
ne = 0
for vi in range(1,6):
    n = int(input())
    if n%2==0:
        p += 1
    else:
        i += 1
    if n>0:
        po += 1
    if n<0:
        ne += 1
print(f'{p} valor(es) par(es)')
print(f'{i} valor(es) impar(es)')
print(f'{po} valor(es) positivo(s)')
print(f'{ne} valor(es) negativo(s)')
