#Faça um programa que leia um ano qualquer e diga se é BISSEXTO
y = int(input('Enter a year: '))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('This is a leap year')
else:
    print('This is NOT a leap year')
