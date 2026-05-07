#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro é maior, o segundo é maior ou os dois são iguais.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

print('Primeiro número: {}'.format(a))
print('Segundo número: {}'.format(b))

if a > b:
    print('O primeiro número é maior que o segundo.')
elif a < b:
    print('O segundo número é maior que o primeiro.')
else:
    print('Os dois números são iguais.')
