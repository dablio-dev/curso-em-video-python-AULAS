from ast import fix_missing_locations

inicio = int (input ('Digite um numero: '))
fim = int (input('Digite o fim: '))
passo = int (input('Digite o passo: '))
for c in range(inicio, fim+1, passo):
    print(c)
print ('FIM')