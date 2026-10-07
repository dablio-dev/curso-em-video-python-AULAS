'''c = 1
while c < 10:
    print(c)
    c+= 1'''

n = 1
totpar = 0
totimpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            totpar += 1
        else:
            totimpar += 1
print(f'Total de numeros pares {totpar}'
      f'\nTotal de numeros impares {totimpar}')
