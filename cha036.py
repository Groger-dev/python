#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou o empréstimo será negado.
from time import sleep
print('_' * 30)
print('Simulação de empréstimo')
print('_' * 30)

casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite qual o seu salário: R$ '))
anos = int(input('Digite em quantos anos deseja pagar: '))
prestacao = casa / (anos * 12)

print('Valor da casa: R${:.2f}'.format(casa))
print('Seu salário: R${:.2f}'.format(salario))
print('Prazo para quitar: {} anos'.format(anos))
print('Parcelas: {}x de R${:.2f}'.format((anos * 12), prestacao))

print('Analisando...')
sleep(3)
if prestacao > (salario * 0.3):
    print('Seu empréstimo foi \33[1;31mnegado\33[m!')
    print('Motivo: o valor da parcela excedeu 30% do seu salário')
else:
    print('Seu empréstimo foi \33[1;32maprovado\33[m!')
    print('Parabéns! Siga os próximos passos para receber a quantia.')
