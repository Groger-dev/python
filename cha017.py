import math

cat1 = eval(input('Digite o comprimento do primeiro cateto: '))
cat2 = eval(input('Digite o comprimento do segundo cateto: '))

# h = math.sqrt(cat1**2 + cat2**2)
# h = (cat1 ** 2 + cat2 ** 2) ** (1/2)
h = math.hypot(cat1, cat2)

print('O comprimento da hipotenusa é igual a: {:.2f}'.format(h))
