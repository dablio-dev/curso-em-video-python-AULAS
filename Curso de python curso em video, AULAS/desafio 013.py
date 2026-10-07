#                   solução com variaveis

# n1=float(input('Digite o salario atual para acrescentar 15%: '))
# acre=n1/100*15
# result=n1+n1/100*15
# print ('Se o salario atual é R${:.2f} o salario passará a ser R${:.2f} após acréscimo de 15%'.format(n1,result))
# print ('Será acrescentado R${:.2f} ao salario!'.format(acre))
#======================================================================
#                      solução com print

n1=float(input('Digite o salario atual para acrescimo de 15%: '))
print ('Se o salario atual é R${:.2f} ele passará a ser R${:.2f} após acrescimo de 15%'.format(n1, n1+n1/100*15))
print ('Será acrescentado R${:.2f} ao salario'.format(n1/100*15))
