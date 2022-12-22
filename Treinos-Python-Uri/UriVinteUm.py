valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(f'{valor}')
for nota in notas:
    qtd_notas = int(valor/nota)
    print(f'{qtd_notas} nota(s) de {nota:.2f}')
    valor -= qtd_notas * nota
