velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade-80) * 7
if velocidade > 80:
    print(f'Você excedeu o limite de velocidade e foi multado em R${multa:.2f}'
          f'\nVocê estava a {velocidade - 80:.1f}Kmh acima do permitido')
