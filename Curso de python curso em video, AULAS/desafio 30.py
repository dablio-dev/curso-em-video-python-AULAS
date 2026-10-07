n1 = int(input('Digite um numero para saber se ele é impar ou par: '))
n2 = n1 % 2
if n2 == 0:
    print (f'O numero {n1} é um numero par')
else:
    print (f'O numero {n1} é um numero impar')
