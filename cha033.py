#Faça um programa que leia três números e diga qual é o maior e o menor
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
c = int(input('Enter another number: '))

if a > b and a > c:
    print('The number {} is the greatest'.format(a))
elif b > a and b > c:
    print('The number {} is the greatest'.format(b))
else:
    print('The number {} is the greatest'.format(c))

if a < b and a < c:
    print('The number {} is the smallest'.format(a))
elif b < a and b < c:
    print('The number {} is the smallest'.format(b))
else:
    print('The number {} is the smallest'.format(c))
