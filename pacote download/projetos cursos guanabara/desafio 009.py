#             SOLUÇÃO FUNCIONAL COM VARIAVEIS

# n1=int(input('Digite um numero: '))
# msg1='Esta é a tabuada de {}'.format(n1)
# x1='{}x1={}'.format(n1, (n1*1))
# x2='{}x2={}'.format(n1, n1*2)
# x3='{}x3={}'.format(n1, n1*3)
# x4='{}x4={}'.format(n1, n1*4)
# x5='{}x5={}'.format(n1, n1*5)
# x6='{}x6={}'.format(n1, n1*6)
# x7='{}x7={}'.format(n1, n1*7)
# x8='{}x8={}'.format(n1, n1*8)
# x9='{}x9={}'.format(n1, n1*9)
# x10='{}x10={}'.format(n1, n1*10)
# print ('{:=^80}'.format(msg1),'\n', x1, '\n', x2, '\n', x3, '\n', x4, '\n', x4, '\n', x5, '\n', x6, '\n', x7, '\n', x8, '\n', x9, '\n', x10)
#==============================================================================================================================================
#            SOLUÇÃO MAIS SIMPLES USANDO APENAS PRINT

n1=int(input('Digte um numero para descobrir a tabuada: '))
msg='Esta é a tabuada de {}'.format(n1)
print ('{:=^80}'.format(msg))
print (' {}x1={}'.format(n1, n1*1), '\n','{}x2={}'.format(n1, n1*2), '\n','{}x3={}'.format(n1, n1*3), '\n','{}x4={}'.format(n1, n1*5))
print (' {}x6={}'.format(n1, n1*6), '\n', '{}x7={}'.format(n1, n1*7), '\n', '{}x8={}'.format(n1, n1*8), '\n', '{}x9={}'.format(n1, n1*9), '\n', '{}x10={}'.format(n1, n1*10))
