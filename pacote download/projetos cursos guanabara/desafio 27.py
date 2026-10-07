nome=input('Digite seu nome completo: ')
split=nome.split()
ultimo=len(split)
print (f'Seu primeiro nome é {split[0]}'
       f' e seu ultimo nome é {split[ultimo - 1]}')
