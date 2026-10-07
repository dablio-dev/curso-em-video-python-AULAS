verde = '\033[;32m'
vermelho = '\033[;31m'
reset = '\033[m'
n1 = int (input ('Primeiro valor: '))
n2 = int (input ('Segundo valor: '))

if n1 > n2:
    print (f'O primeiro valor ({verde}{n1}{reset}) é maior que o segundo valor ({vermelho}{n2}{reset})!')
elif n2 > n1:
    print (f'O segundo valor ({verde}{n2}{reset}) é maior que o primeiro valor ({vermelho}{n1}{reset})!')
else:
    print ('Os dois valores são iguais!')
