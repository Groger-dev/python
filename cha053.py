#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando espaços
#Feito a partir da resolução do professor
frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
junto = ''.join(separar)
inverso = junto[::-1]
'''inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase digitada é um PALÍNDROMO')
else:
    print('A frase digitada não é um PALÍNDROMO')
