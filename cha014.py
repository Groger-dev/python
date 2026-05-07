#Conversor de temperatura ºC para ºF

t = float(input('Insira a temperatura em Celsius: '))

conv = 9 * t / 5 + 32
#Or conv = t * 1.8 + 32

print('A temperatura é {:.1f} ºF'.format(conv))
