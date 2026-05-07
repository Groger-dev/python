#Escreva um programa que faça o pc "pensar" em um número entre 0 e 5 e peça para o user tentar descobrir o número escolhido
#O programa deverá exibir o resultado, se o user acertou ou errou
from random import randint
from time import sleep
print('Welcome to Challenge *** Discover the number ***')

print('Try discover the right number now!')
print('-=-' * 20)
choice = int(input('Type one number between 0 and 5: '))
number = randint(0, 5)
print('-=-' * 20)
print('Processing...')

sleep(3)

if choice == number:
    print('Congrats! You got it!')
else:
    print('Sorry, you lose')
