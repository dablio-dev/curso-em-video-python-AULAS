from random import choice
from time import sleep


opcoes = ['pedra', 'papel', 'tesoura']
escolha_pc = choice(opcoes)

vermelho = '\033[1;31m'
azul = '\033[1;34m'
verde = '\033[1;32m'
reset = '\033[m'

print(f'{azul}Jogue pedra, papel e tesoura (jokenpô) com seu computador{reset}'.center(80))
sleep(2)
print ('\n')
print (f'{azul}O computador esta escolhendo...{reset}')
sleep(2)
print (f'{azul}O computador já fez sua escolha!{reset} ')
sleep(1)
print (f'\n \nAgora é a sua vez')
escolha_player = str (input('Faça a sua escolha (pedra, papel ou tesoura): ')).strip().lower()

msg = 0

if escolha_pc == 'pedra' and escolha_player == 'tesoura':
    msg = f'O computador escolheu {azul}{escolha_pc}{reset}! Você {vermelho}PERDEU{reset}!'
elif escolha_pc == 'tesoura' and escolha_player == 'papel':
    msg = f'O computador escolheu {azul}{escolha_pc}{reset}! Você {vermelho}PERDEU{reset}!'
elif escolha_pc == 'papel' and escolha_player == 'pedra':
    msg = f'O computador escolheu {azul}{escolha_pc}{reset}! Você {vermelho}PERDEU{reset}!'
elif escolha_pc == escolha_player:
    msg = f'O computador escolheu {azul}{escolha_pc}{reset}! Ambos escolheram o mesmo! Vocês \033[1;33mEMPATARAM{reset}'
else:
    msg = f'O computador escolheu {azul}{escolha_pc}{reset}! Você {verde}VENCEU{reset}'
print ('\n')
print(f'{azul}' + f' RESULTADO '.center(80, '='), f'{reset}')
print(msg)
print('='*80)
