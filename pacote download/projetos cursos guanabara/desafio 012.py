#                    solução com variaveis

# n1=float(input('Digite o valor do seu produto para aplicar um desconto de 5%: '))
# result=n1-n1/100*5
# desc=n1/100*5
# print ('Se seu produto custa atualmente R${:.2f} ele custará R${:.2f} após desconto de 5%!'.format(n1,result))
# print ('Com esse desconto você economiza R${:.2f}'.format(desc))
#===========================================================================================
#                            solução apenas com print
n1=float(input('Digite o valor do seu produto para aplicar um desconto de 5%: '))
print ('Se seu produto custa R${:.2f} ele custará R${:.2f} após desconto de 5%'.format(n1,n1-n1/100*5))
print ('Após aplicar o desconto você estará economizando R${:.2f}'.format(n1/100*5))
