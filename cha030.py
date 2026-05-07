#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
num = int(input('Type a number: '))
print('You typed {}'.format(num))
if num % 2 == 0:
    print('This number is even')
else:
    print('This number is odd')
