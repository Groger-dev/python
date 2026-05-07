#Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso.
#Feito com auxílio do professor
maior = 0
menor = 0
for pessoas in range (1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso foi {:.1f}Kg'.format(maior))
print('O menor peso foi {:.1f}Kg'.format(menor))
