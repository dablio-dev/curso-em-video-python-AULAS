vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
reset = '\033[m'

valor_produto = float (input ('Valor do produto: R$ '))

forma_pagamento = int (input (f'\nForma de pagamento: \n[1] pix/dinheiro | {verde}10% de DESCONTO{reset}'
                              f'\n[2] avista no cartão | {azul}5% de DESCONTO{reset}'
                              f'\n[3] até 2x no cartão | {amarelo}Preço NORMAL{reset}'
                              f'\n[4] 3x ou mais no cartão | {vermelho}20% de JUROS{reset}'
                              f'\nDigite o numero equivalente a sua forma de pagamento: '))

final = 0
desconto = 0
msg = 0
forma = 0

if forma_pagamento == 1:
    desconto = valor_produto / 100 * 10
    final = valor_produto - desconto
    forma = 'Pix/Dinheiro'
    msg = f'{verde}10% de DESCONTO{reset}'
elif forma_pagamento == 2:
    desconto = valor_produto / 100 * 5
    final = valor_produto - desconto
    forma = 'Avista no cartão'
    msg = f'{azul}5% de DESCONTO{reset}'
elif forma_pagamento == 3:
    final = valor_produto
    forma = 'Até 2x no cartão'
    desconto = 0.00
    msg = f'{amarelo}Preço NORMAL{reset}'
elif forma_pagamento == 4:
    desconto = valor_produto / 100 * 20
    final = valor_produto + desconto
    forma = '3x ou mais no cartão'
    msg = f'{vermelho}20% de JUROS{reset}'

print ('\n')
print ('Comprovante de pagamento'.center(60, '='))
print (f'Valor do produto: {azul}R$ {valor_produto:.2f}{reset}'
       f'\nForma de pagamento escolhida: {forma}'
       f'\nDesconto/juros aplicado: {msg}'
       f'\nValor descontado: R$ {desconto:.2f}'
       f'\nTotal a pagar: {verde}R$ {final:.2f}{reset}')
print('=' * 60)
