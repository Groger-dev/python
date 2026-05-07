#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
#1 - binário
#2 - octal
#3 - hexadecimal

num = int(input('Digite um número: '))
print('Converter para:\n 1 - binário\n 2 - octal\n 3 - hexadecimal')
escolha = int(input('Qual a sua escolha: '))

if escolha == 1:
    convert = bin(num)
    print('O número {} em binário é {}'.format(num, convert [2:]))
elif escolha == 2:
    convert = oct(num)
    print('O número {} em octal é {}'.format(num, convert [2:]))
elif escolha == 3:
    convert = hex(num)
    print('O número {} em hexadecimal é {}'.format(num, convert[2:]))
else:
    print('Opção inválida!Tente novamente')
print('Fim')
