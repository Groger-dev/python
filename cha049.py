#Refaça a tabuada do cha009, usando um número que o usuário escolher para a tabuada. Ultilize o for para isso

num = int(input('Digite um número para calcular sua tabuada: '))

for n in range(1, 11):
    print('{} x {:>3} = {:>3}'.format(num, n, num * n))
print('Fim')
