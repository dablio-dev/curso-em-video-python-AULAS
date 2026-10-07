#                         SOLUÇÃO USANDO VARIAVEIS

# n1=float(input('Digite uma distancia em metros (em caso de um numero real separe apenas por ponto "."): '))
# cen=int(n1*100)
# mil=int(n1*1000)
# print ('{}m equivale a {} centimetros \n{}m equivale a {} milimetros'.format(n1,cen,n1,mil))
#------------------------------------------------------------------------------------------------
#                                          SOLUÇÃO USANDO PRINT

n1=float(input('Digite uma distancia em metros (em caso de um numero real separe apenas por ponto "."): '))
print (n1,'metros equivale a', (int(n1*100)),'centimetros\n',n1, 'metros equivale a', (int(n1*1000)), 'milimetros')
# não consigo uma forma de usar o .format sem usar variaveis para preencher as {}, não quero atropelar as aulas confio no ritmo do professoar