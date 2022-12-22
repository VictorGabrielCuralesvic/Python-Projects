i = int(input())
x = int(i)

a = int(x/365)
x = x%365

m = int(x/30)
x = x%30

d = x

print(f'\n{a} ano(s)\n{m} mes(es)\n{d} dia(s)')