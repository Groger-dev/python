#Crie um programa que faça o computador jogar Jokenpô com você
from random import choice
from time import sleep
print('-*-' * 10)
print('\33[1;32m          Jokenpô\33[m')
print('-*-' * 10)

lista = ['pedra', 'papel', 'tesoura']
jpc = choice(lista)
print('Pedra, papel ou tesoura?')
jus = str(input('Digite a sua escolha: ')).strip().lower()

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Poooo!!')

print('PC = {} e User = {}'.format(jpc, jus))

if jpc == 'pedra' and jus == 'papel':
    print('Você ganhou!')
elif jpc == 'pedra' and jus == 'tesoura':
    print('Você perdeu!')
elif jpc == 'papel' and jus == 'pedra':
    print('Você perdeu!')
elif jpc == 'papel' and jus == 'tesoura':
    print('Você ganhou!')
elif jpc == 'tesoura' and jus == 'pedra':
    print('Você ganhou!')
elif jpc == 'tesoura' and jus == 'papel':
    print('Você perdeu!')
else:
    print('Empate')
