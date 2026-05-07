#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre:
#A média de idade
#O nome do homem mais velho
#Quantas mulheres tem menos de 20 anos
soma = 0
idvelho = 0
nomevelho = ''
mjovens = 0
for p in range(1, 5):
    print('-' * 20)
    print('{}ª pessoa'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if p ==1 and sexo in 'Mm':
        idvelho = idade
        nomevelho = nome
    else:
        if idade > idvelho:
            idvelho = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mjovens += 1
print('A média da idade das 4 pessoas é de {} anos'.format(int(soma/4)))
print('{} é o homem mais velho do grupo e tem {} anos'.format(nomevelho, idvelho))
print('No grupo há {} mulher(es) menor(es) de 20 anos'.format(mjovens))
