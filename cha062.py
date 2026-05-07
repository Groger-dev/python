#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Arithmetic progression v3.0')
print('-*-' * 10)
t = int(input('The first term: '))
d = int(input('Common difference: '))
count = 0
s = t
end = 10
cont = ''
while count < end:
    print('{}'.format(s), end=' → ')
    s += d
    count += 1
    if count == end:
        cont = str(input('\nDo you want to continue?[Y/N] '))
        if cont in 'Yy':
            Nend = int(input('Type how many terms: '))
            end = end + Nend
        elif cont in 'Nn':
            break
        else:
            print('Invalid input')
            count -= 1
            s -= d
print('-=-' * 10)
print('Total terms showing: {}'.format(count))
print('End')
