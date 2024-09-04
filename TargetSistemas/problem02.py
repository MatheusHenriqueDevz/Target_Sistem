n = int(input('Digigte a quantidade de termos da séria de Fibonacci: '))

a = 0
b = 1
f = 0

print(a)

for i in range(n-1):
    if (i%2)==0:
        a=f

if (i%2)==1:
    b=f

f = a + b