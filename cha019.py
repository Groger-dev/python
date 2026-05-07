import random

a = input('Insira o nome do primeiro aluno: ')
b = input('Insira o nome do segundo aluno: ')
c = input('Insira o nome do terceiro aluno: ')
d = input('Insira o nome do quarto aluno: ')

#Pulo do gato kkkk não é essa a solução, mas valeu a intenção
num = random.randint(1, 4)

#print('1 - {}'.format(a))
#print('2 - {}'.format(b))
#print('3 - {}'.format(c))
#print('4 - {}'.format(d))
print('O aluno(a) escolhido foi {}'.format(num))