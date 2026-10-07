n1=input('Digite seu nome completo')
n2=n1.split()
n3=''.join(n2)
print(f'Nome com todas as letra minusculas {n1.lower()}'
      f'\nNome com todas as letras maiuscula {n1.upper()}'
      f'\nQuantas letras sem espaços {len(n3)}'
      f'\nQuantas letras tem o primeiro nome {len(n2[0])}')
