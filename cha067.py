# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
t = 'Tabuada'
print('-*-'*20)
print(t.center(60))
print('-*-'*20)
num = 1
while num > 0:
    num = int(input('Type a positive number (negative to exit): '))
    if num < 0:
        break
    for n in range(1,11):
        print('{} x {:>2} = {:>3}'.format(num, n, num * n))
print('End')
