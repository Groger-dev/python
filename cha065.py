#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = int(input('Type a number: '))
choice = str(input('Do you wanna continue?[Y/N] ')).upper().strip()[0]
sum = big = small = num
count = 1
while choice != 'N':
    num = int(input('Type other number: '))
    if num > big:
        big = num
    if num < small:
        small = num
    sum += num
    count += 1
    choice = str(input('Do you wanna continue?[Y/N] ')).upper().strip()[0]
print('The bigger number is: {}'.format(big))
print('The smaller number is: {}'.format(small))
print('The sum of all numbers is: {}'.format(sum))
print('You typed {} numbers'.format(count))
print('The average is: {}'.format(sum / count))
