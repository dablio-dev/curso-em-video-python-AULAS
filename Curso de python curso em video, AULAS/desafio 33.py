n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 > n2 and n1 >  n3:
    maior = n1
else:
    if n1 < n2 and n1 < n3:
        menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
else:
    if n2 < n1 and n2 < n3:
        menor = n2
if n3 > n1 and n3 > n2:
    maior = n3
else:
    if n3 < n1 and n3 < n2:
        menor = n3
print (f'O maior entre os três é {maior} e o menor é {menor}!')
