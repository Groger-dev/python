# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
soma = contador = vitorias = 0
while True:
    escolha = ' '
    while escolha not in 'IÍP':
        escolha = str(input('Ímpar ou par?[I/P] ')).strip().upper()[0]
    jogador = int(input('Escolha um número entre 0 e 5: '))
    pc = randint(0,5)
    soma = jogador + pc
    print(f'Você escolheu o número {jogador} e o PC {pc} a soma dos dois {soma}.', end = ' ')
    print(f'Deu par!' if soma % 2 == 0 else 'Deu ímpar!')
    if escolha in 'IÍ':
        if soma % 2 == 1:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    elif escolha == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
print('_' * 15)
print(f'Total de acertos: {vitorias}')
