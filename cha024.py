#Crie um programa que leia o nome de uma cidade e diga se ela começa com 'santo'

cid = str(input('Insira o nome da cidade: ')).strip()
print(cid[:5].lower() == 'santo')
