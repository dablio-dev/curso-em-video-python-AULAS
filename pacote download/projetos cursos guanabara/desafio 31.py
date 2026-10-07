'''distancia = float(input('Digite a distancia da sua viagem em km: '))
if distancia <= 200:
    preco=distancia*0.50
else:
    preco=distancia*0.45
print (f'Você viajou {distancia:.1f}Km e vai pagar R${preco:.2f}')'''

distancia = float(input('Digite a distancia percorrida da viajem em Km: '))
if distancia <= 200:
    print (f'Sua viajem foi de {distancia:.1f}Km e você pagará R$0,50 em cada Km totalizando R${distancia*0.50:.2f}')
else:
    print (f'Sua viajem foi de {distancia:.1f}Km e você pagará R$0,45 em cada Km totalizando R${distancia*0.45:.2f}')
