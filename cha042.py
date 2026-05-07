#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar o tipo de triângulo formado:
#Equilátero
#Isósceles
#Escaleno

#Ctrl + C Ctrl + v hehehe
print('Type three measures in cm for discover if can be a triangle')
a = float(input('First side: '))
b = float(input('Second side: '))
c = float(input('Third side: '))
if a < b + c and b < a + c and c < a + b:
    print('\33[1;32mThe triangle is possible!\33[m')
    if a == b == c:
        print('This is a equilateral triangle!')
    elif a == b or b == c or c == a:
        print('This is a isosceles triangle!')
    else:
        print('This is a scalene triangle!')
else:
    print('\33[1;31mThe triangle is NOT possible!\33[m')

