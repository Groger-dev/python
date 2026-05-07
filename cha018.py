#calculadora de seno, cosseno e tangente
import math

ang = float(input('Digite o valor do ângulo em graus: '))
#o cálculo feito pelas funções math.sin, math.cos e math.tan consideram a medida do ângulo em radianos e não graus

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno do ângulo {}º é {:.2f}'.format(ang, sen))
print('Seu cosseno é {:.2f}'.format(cos))
print('E sua tangente {:.2f}'.format(tan))
