import random
print ('Avinhe o numero gerado')
n1 = random.randint (0,5)
print ('Gerando numero ...')
r = int(input('Digite um numero e tente adivinhar o numero de 0 a 5 que o programa gerou: '))
if r == n1:
    print ('Parabens, você acertou!')
else:
    print ('Que pena você errou, tente mais uma vez! ')
print (f'O numero gerado foi {n1}')
