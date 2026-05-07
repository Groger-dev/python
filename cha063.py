#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
print('-=-' * 10)
print('Fibonacci sequence')
print('-=-' * 10)
terms = int(input('How many terms do you want to see? '))
t1 = 0
t2 = 1
count = 3
print('{} → {}'.format(t1, t2), end=' → ')
while count <= terms:
    tn = t1 + t2
    print('{}'.format(tn), end=' → ')
    t1 = t2
    t2 = tn
    count += 1
print('Fim')
