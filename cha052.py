#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))

for c in range(2, num + 1):
    if c % 3 == 0 and num % c == 0 or num % 2 == 0:
        print('O número {} não é primo'.format(num))
        break
    else:
        print('O número {} é primo'.format(num))
        break
print('FAIL')
