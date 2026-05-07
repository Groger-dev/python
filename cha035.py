#Desenvolva um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo
print('Type three measures in cm for discover if can be a triangle')
a = float(input('First side: '))
b = float(input('Second side: '))
c = float(input('Third side: '))
if a < b + c and b < a + c and c < a + b:
    print('\33[1;32mThe triangle is possible!\33[m')
else:
    print('\33[1;31mThe triangle is NOT possible!\33[m')
print('***END***')
