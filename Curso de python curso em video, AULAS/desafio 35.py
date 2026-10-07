r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de outra reta: '))
r3 = float(input('Digite o comprimento de outra reta: '))
if (r1 + r2 > r3) and (r3 + r2 > r1) and (r3 + r1 > r2):
    print ('Podem formar um triângulo')
else:
    print ('Não podem formar um triângulo')
