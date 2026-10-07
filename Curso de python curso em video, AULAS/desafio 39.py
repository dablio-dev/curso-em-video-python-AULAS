from datetime import date

amarelo = '\033[;33m'
vermelho = '\033[;31m'
verde = '\033[;32m'
reset = '\033[m'

ano_nascimento = int (input ('Ano de nascimento :'))

este_ano = date.today()
anostr = str (este_ano)
anofmt = int (anostr[:4])
result = anofmt - ano_nascimento
falta = 0
passou = 0

if result < 18:
    falta = 18 - result
    print (f'{amarelo}AINDA NÃO{reset} chegou sua hora de se alistar, seu alistamento será em {falta} anos! ')
elif result == 18:
    print (f'{verde}ESTE É O ANO DO SEU ALISTAMENTO !{reset} Compareça em uma unidade militar!')
else:
    passou = result - 18
    print (f'{vermelho}SEU ANO DE ALISTAMENTO PASSOU !{reset} Se ainda não se alistou você passou {passou} nos do tempo!')
