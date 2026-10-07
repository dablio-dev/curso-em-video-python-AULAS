nome = str (input('Qual é seu nome ?:')).title()
if nome == 'Wesley':
    print ('Que nome bonito!')
elif nome == 'Bia' or nome =='Jamily' or nome == 'Lorranny':
    print ('Seu nome é bem importante!')
elif nome in 'Ana Claudia Jessica Juliana':
    print ('Belo nome feminino')
else:
    print ('Seu nome é bem normal')
print (f'Tenha um bom dia, {nome}!')
