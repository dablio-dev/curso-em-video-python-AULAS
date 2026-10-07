ano = int(input('Digite um ano e descubra se ele é bissexto: '))
ano2 = ano % 4
if ano2 == 0:
    ano3 = ano % 100
    if ano3 == 0:
        ano4 = ano % 400
        if ano4 == 0:
            print (f'O ano {ano} é um ano bissexto')
        else:
            print (f'O ano {ano} não é um ano bissexto!')
    else:
        print (f'O ano {ano} é um ano bissexto')
else:
    print (f'O ano {ano} não é um ano bissexto!')

