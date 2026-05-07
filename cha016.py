import math

num = float(input('Digite um número real: '))
print('O número {} na sua forma inteira é {}'.format(num, math.floor(num)))
print('O número digitado é {} e sua forma inteira é {}'.format(num, math.trunc(num)))
print('O número {} na sua forma inteira é {}'.format(num, int(num)))
