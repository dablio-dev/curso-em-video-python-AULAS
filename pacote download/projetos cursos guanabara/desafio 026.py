frase=input('Digite uma frase: ')
frase2=frase.lower()
print (f'Nesta frase a letra "A" aparece {frase2.count('a')} vezes!'
       f'\nNesta frase a letra "A" aparece primeiro na casa {frase2.find('a')}!'
       f'\nNesta frase a letra "A" aparece por ultimo na casa {frase2.rfind('a')}!')
