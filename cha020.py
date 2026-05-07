#Ordenar uma sequência de alunos para executar uma tarefa
import random
a = input('Digite o nome do(a) aluno(a): ')
b = input('Digite o nome do(a) aluno(a): ')
c = input('Digite o nome do(a) aluno(a): ')
d = input('Digite o nome do(a) aluno(a): ')

lista = [a, b, c, d]
random.shuffle(lista)

print('A ordem dos alunos para a tarefa será: \n{}'.format(lista))
