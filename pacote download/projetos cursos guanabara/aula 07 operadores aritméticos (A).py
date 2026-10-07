n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma vale: {},\n o produto é: {} \n a divisão é: {:.3}'.format(s, m, d), end='>>>')
print ('Divisão inteira: {}, potencia: {}'.format(di,e))
