#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Arithmetic progression')
print('-=-' * 8)
t = int(input('The first term: '))
d = int(input('Common difference: '))
count = 1
s = t
while count < 10:
    print('{}'.format(s), end =' → ')
    s += d
    count += 1
print('END')
