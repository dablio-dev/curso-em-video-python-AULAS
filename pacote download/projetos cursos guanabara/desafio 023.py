n1=int(input('Digite um numero entre 0 e 9999: '))
n2=f'{n1:04d}'
print (n2)
print (f'Este numero tem'
       f'\nUnudades {n2[3]}'
       f'\nDezenas {n2[2]}'
       f'\nCentenas {n2[1]}'
       f'\nMilhares {n2[0]}')
