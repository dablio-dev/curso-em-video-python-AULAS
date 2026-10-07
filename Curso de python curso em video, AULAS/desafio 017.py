from math import pow, sqrt
print ('Descubra o cumprimento da hipotenusa')
n1=float(input('Digite o cumprimento do cateto oposto: '))
n2=float(input('digite o cateto adjecente: '))

n3=(n1**2 + n2**2) ** 0.5

# SOLUÇÕES ALTERNATIVAS USANDO O MODULO MATH E OUTROS TIPOS DE OPERAÇÕES
# cat=pow(n1, 2) + pow(n2, 2)
# cat=n1**2 + n2**2
# result= (sqrt(cat))
# result=cat**0.5
# result=cat**(1/2)

print ('A hipotenusa deste triangulo retangulo é {}'.format(n3))
