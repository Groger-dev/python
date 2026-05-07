#Crie um programa que leia dois números e mostre um menu:
#[1] somar; [2] multiplicar; [3] mostrar o maior; [4] novos números; [5] sair;
#Seu programa deverá a operação indicada em cada caso
from time import sleep
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
escolha = 0
while escolha != 5:
    sleep(2)
    print('O que você quer fazer com esses dois números?')
    print('''[1] somar
[2] multiplicar
[3] mostrar o maior
[4] novos números
[5] sair''')
    escolha = int(input('Digite a sua escolha: '))
    sleep(1)

    if escolha == 1:
        soma = a + b
        print('A soma entre {} e {} é {}'.format(a, b, soma))
    elif escolha == 2:
        multiplicar = a * b
        print('{} x {} = {}'.format(a, b, multiplicar))
    elif escolha == 3:
        if a > b:
            maior = a
            print('O maior número é {}'.format(maior))
        elif a < b:
            maior = b
            print('O maior número é {}'.format(maior))
        else:
            print('Os dois números são iguais')
    elif escolha == 4:
        print('Você escolheu digitar novos números')
        a = int(input('Digite o primeiro número: '))
        b = int(input('Digite o segundo número: '))
    elif escolha > 5 or escolha == 0:
        print('Opção inválida! Tente novamente')
print('Saindo...')
sleep(2)
print('Até mais!')
