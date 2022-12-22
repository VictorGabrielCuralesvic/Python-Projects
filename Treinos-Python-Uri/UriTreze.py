lulu = input().split()
r = float(input("insira o raio: "))
a = float(lulu[0])
b = float(lulu[1])
c = float(lulu[2])
pi = 3.14159

at = (a * c)/2.0
ac = (pi * r**2)
atr = ((a + b)*c/2.0)
aq = (b**2)
ar = (a*b)

print('TRIANGULO: {:.3f}'.format(at))
print('CIRCULO: {:.3f}'.format(ac))
print('TRAPEZIO: {:.3f}'.format(atr))
print('QUADRADO: {:.3f}'.format(aq))
print('RETANGULO: {:.3f}'.format(ar))
