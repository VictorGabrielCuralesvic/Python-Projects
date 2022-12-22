n = int(input())
a = int(n)

h = int(a/3600)
a = a%3600

m = int(a/60)
a = a%60

s = a

print(f'{h}'+':'+f'{m}'+f':'+f'{s}')