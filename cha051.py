#Desenvolva um programa que leia o primeiro termo e a razão de um PA. No fim mostre os primeiros 10 termos dessa progressão.

t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for p in range(t, (t + (10 * r)), r):
    print(p, end=' → ')
print('FIM')
