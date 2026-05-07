#Faça um programa que leia um número e mostre seu fatorial
'''from math import factorial
num = int(input('Type a number: '))
f = factorial(num)
print('The factorial of {} is {}'.format(num, f))'''
num = int(input('Type a number: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end = '')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c #aqui a ordem faz muita diferença, caso a variável 'c' venha primeiro a 'f' retornará igual a 0 no fim da execução
    c -= 1
print('{}'.format(f))
