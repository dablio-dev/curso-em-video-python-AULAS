#                       SOLUÇÃO COM VARIAVEIS

# n1=float(input('Qual é a altura da sua parede em metros: '))
# n2=float(input('Qual é a largura da sua parede em metros: '))
# area=n1*n2
# result=area/2
# print ('Se sua parede tem {:.2f} de altura e {:.2f} de largura ela tem {:.2f}m² e se cada litro de tinta consegue pintar 2m² de parede\nvocê vai usar {:.2f} litros de tinta para pintar toda a parede'.format(n1,n2,area,result))
#==================================================================================
#                    SOLUÇÃO SEM VARIAVEIS, APENAS PRINT

n1=float(input('Digite a altura da parede em metros: '))
n2=float(input('Digite a largura da parede em metros: '))
print ('Se sua parede tem {:.2f} metros de altura e {:.2f} metros de largura ela tem {:.2f}m².'.format(n1,n2,n1*n2))
print ('Se cada litro de tinta pinta 2m² você vai precisa de {:.2f} litros de tinta para pintar esta parede por completo.'. format(n1*n2/2))
