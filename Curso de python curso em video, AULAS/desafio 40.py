primeiro_nota = float (input('Primeira nota: '))
segunda_nota = float (input('Segunda nota: '))

media = (primeiro_nota + segunda_nota) / 2

if media < 5:
    msg = '\033[1;31mREPROVADO\033[m!'
elif 5 <= media <= 6.9:
    msg = '\033[1;33mEM RECUPERAÇÃO\033[m'
else:
    msg = '\033[1;32mAPROVADO\033[m'

print (f'Com a media \033[1;34m{media:.1f}\033[m este aluno esta {msg}!')
