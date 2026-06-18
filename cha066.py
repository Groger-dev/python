# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

num = count = sum = 0
while num != 999:
    num = int(input('Type a number (999 for stop): '))
    if num == 999:
        break
    count += 1
    sum += num
print('You typed {} numbers and the sum between them is {}'.format(count, sum))
