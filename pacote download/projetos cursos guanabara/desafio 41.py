from datetime import date

ano = int(input('Ano de nascimento do atleta: '))

ano_atual = date.today()
ano_str = str (ano_atual)
ano_fmt = int (ano_str[:4])

idade = ano_fmt - ano
categoria = 0

if idade <= 9:
    categoria = 'MIRIM'
elif 9 < idade <= 14:
    categoria = 'INFANTIL'
elif 14 < idade <= 19:
    categoria = 'JUNIOR'
elif 19 < idade <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print (f'Este atleta tem \033[1;34m{idade}\033[m anos e atua na categoria \033[1;32m{categoria}\033[m!')