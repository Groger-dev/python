#Crie um programa que leia o ano de nascimento de 7 pessoas. No final diga quantas ainda não atingiram a maioridade e quantas já são maiores
#Maoridade = 21 anos
from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for a in range(1, 8):
    ano = int(input('Ano de nascimento da pessoa {}: '.format(a)))
    if atual - ano >= 21:
        maiores +=1
    else:
        menores +=1
print('Das sete pessoas {} atingiram a maioridade'.format(maiores))
print('E {} não atingiram a maoridade'.format(menores))
