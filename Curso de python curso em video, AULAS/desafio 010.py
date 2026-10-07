#                               SOLUÇÃO 1 COM VARIAVEL PARA O RESULTADO

# n1=float(input('Digite a quantidade de R$ (reais) que você possui para descobrir quantos U$ (dollars) você pode comprar: '))
# result = n1/3.27
# print ('Com R$ {:.2f} você consegue comprar U$ {:.2f}'.format(n1, result))
#======================================================================================

#SOLUÇÃO 2 SEM VARIAVEL PARA O RESULTADO OPERAÇÃO FEITA NO PRINT

n1=float(input('Digite a quantidade de R$ (reais) que você possui para descobrir quantos U$ (dollars) você pode comprar: '))
print ('Com R${:.2f} você consegue comprar U${:.2f} a 3,27 cada!'.format(n1, n1/3.27))
