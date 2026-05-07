#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar desconsidere-o
soma = 0
for n in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
print('Soma dos números pares: {}'.format(soma))
print('Fim')
