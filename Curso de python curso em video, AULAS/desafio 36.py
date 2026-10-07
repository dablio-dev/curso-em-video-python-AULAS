from math import ceil

vermelho = '\033[1;31;48m'
verde = '\033[1;32;48m'
reset = '\033[m'

valor_casa = float (input ('Valor da casa: R$ '))
salario_comprador = float (input ('Salario do comprador: R$ '))
parcelas_anos = float (input ('Tempo de financiamento (anos): '))

parcelas = valor_casa / parcelas_anos / 12
msg = 0
meses = ceil (parcelas_anos * 12)
if parcelas > (salario_comprador / 100 * 30):
    msg = f'Seu financiamento foi {vermelho}NEGADO{reset}, pois o valor do financiamento excede 30% da sua renda '
else:
    msg = f'Parabens! Seu financiamento foi {verde}APROVADO{reset}'
print ('\n')
print (' Resumo do financiamento '.center (90, '='))
print(msg)
print (f'Você financiou a casa em: {parcelas_anos} anos | {meses} meses.'
       f'\nO valor de cada parcela sai a: {verde}R$ {parcelas:.2f}{reset}'
       f'\nIsso equivale a: \033[1;34;48m{parcelas / salario_comprador * 100:.2f}%{reset} do seu salario de {verde}R$ {salario_comprador:.2f}{reset}')
print ('='*90)