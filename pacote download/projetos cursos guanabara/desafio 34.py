salario = float(input('Digite o valor do salario para adicionar um acréscimo: '))

if salario > 1250.00:
    aumento10 = salario / 100 * 10 + salario
    print (f'O salario inicial era R${salario:.2f} e passou a ser {aumento10:.2f} após acréscimo de 10%')
else:
    aumento15 = salario / 100 * 15 + salario
    print (f'O salario inicial era R${salario:.2f} e passou a ser R${aumento15:.2f} após aumento de 15%')
