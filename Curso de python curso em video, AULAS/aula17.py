a = [2, 3, 4, 7]
b = a[:]
b[1] = 1
print(f'Lista A: {a}')
print(f'Lista B: {b}')

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for chave, valor in enumerate(valores):
    print(f'Na posição {chave} eu encontrei o valor {valor}!')'''

'''valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for chave, valor in enumerate(valores):
    print(f'Na posição {chave}, eu encontrei o valor {valor}! ')'''


'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')'''