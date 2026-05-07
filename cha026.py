#Faça um programa que leia uma frase pelo teclado e mostre:
#1. Quantas vezes aparece a letra 'a'
#2. Em que posição ela aparece a primeira vez
#3. Em que posição ela aparece a última vez

phrase = str(input('Type a phrase: ')).strip()
#phrase = phrase.lower() - this is not necessary

print('In this phrase we found {} *a'.format(phrase.lower().count('a')))
print('The first *a is on the position {}'.format(phrase.lower().find('a')))
print('The last *a is on the position {}'.format(phrase.lower().rfind('a')))
