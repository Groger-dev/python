#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria de acordo com a idade
#Até 9 anos - MIRIM
#Até 14 anos - INFANTIL
#Até 19 anos - JUNIOR
#Até 25 - SÊNIOR
#Acima - MASTER
from datetime import date
y = date.today().year
b = int(input('Em que ano você nasceu? '))
a = y - b
print('Se você nasceu no ano {} então você completa {} anos neste ano'.format(b, a))

if a <= 9:
    print('Grupo: MIRIM')
elif a <= 14:
    print('Grupo: INFANTIL')
elif a <= 19:
    print('Grupo: JUNIOR')
elif a <= 25:
    print('Grupo: SÊNIOR')
else:
    print('Grupo: MASTER')
