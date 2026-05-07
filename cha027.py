#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome

name = str(input('Type your complete name: '))

print('Your first name is {}'.format(name[0:(name.find(' ')+1)]))
print('Your last name is {}'.format(name[(name.rfind(' ')+1):]))
