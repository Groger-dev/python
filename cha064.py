#Crie um programa que leia vários números inteiros pelo teclado .
#O programa só vai parar quando o usuário digitar o valor 9999, que é a condição de parada (flag).
#No final, mostre quantos números foram digitados e a soma entre eles (desconsiderando o flag).

i = 0
count = 0
sum = 0
#Pode ser simplificado por i = count = sum = 0
while i != 9999:
    i = int(input('Type a number (9999 to exit): '))
    if i == 9999:
        break
    else:
        count += 1
        sum += i

print('You entered {} numbers'.format(count))
print('The total sum is {}'.format(sum))
