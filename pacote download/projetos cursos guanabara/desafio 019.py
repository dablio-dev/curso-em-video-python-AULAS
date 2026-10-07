from random import choice
n1=input('Digite o primeiro nome do sorteio: ')
n2=input('Digite o segundo nome do sorteio: ')
n3=input('Digite o terceiro nome do sorteio: ')
n4=input('Digite o quarto nome do sorteio: ')
grupo=n1, n2, n3, n4
print ('O resultado do sorteio é {}'.format(choice(grupo)))
