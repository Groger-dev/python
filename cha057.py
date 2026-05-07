#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até a inserção de um valor correto.
sexo = 'd'
while sexo not in 'MmFf':
    sexo = str(input('Digite seu sexo [M/F]: ')).strip()
    if sexo not in 'MmFf':
        print('Digite novamente')
print('Fim')
