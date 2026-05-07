#Escreva um programa que pergunte o salário de um funcionário e calcule o seu aumento.
#Para salários acima de R$1.250,00, calcule um aumento de 10%
#Para salários inferiores calcule um aumento de 15%
s = float(input('What is your salary? $'))
if s > 1250.00:
    ns = s * 1.10
    print('You will receive a raise of ${:.2f}\nTherefore, your new salary will be ${:.2f}'.format(s * 0.10, ns))
else:
    ns = s * 1.15
    print('You will receive a raise of ${:.2f}\nTherefore, your new salary will be ${:.2f}'.format(s * 0.15, ns))
print('Congratulaions for your raise! Good work!')
