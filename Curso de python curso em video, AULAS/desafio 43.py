vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
reset = '\033[m'

altura = float (input ('Altura do paciente (metros): '))
peso = float (input ('Peso do paciente (kg): '))

imc = peso / (altura * altura)

msg = 0

if imc < 18.5:
    msg = f'{amarelo}abaixo do peso{reset}'
elif 18.5 < imc < 25:
    msg = f'{verde}peso ideal{reset}'
elif 25 <= imc <= 30:
    msg = f'{amarelo}sobrepeso{reset}'
elif 30 < imc <= 40:
    msg = f'{vermelho}obesidade{reset}'
elif imc > 40:
    msg = f'{vermelho}obesidade mórbida{reset}'
print (f'Com o imc \033[1;34m{imc:.2f}{reset}, o paciente se encontra no status: {msg}!')
