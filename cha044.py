#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#À vista no dinheiro/pix: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

v = float(input('Digite o preço normal do produto: '))
print('Formas de pagamento:\n1 - À vista no dinheiro/pix: 10% de desconto\n2 - À vista no cartão: 5% de desconto')
print('3 - Em até 2x no cartão: preço normal\n4 - 3x ou mais no cartão: 20% de juros')
e = int(input('Digite a sua opção de pagamento: '))

if e == 1:
    vf = v * 0.9
    print('Total a ser pago: R$ {:.2f}'.format(v * 0.9))
elif e == 2:
    vf = v * 0.95
    print('Total a ser pago: R$ {:.2f}'.format(v * 0.95))
elif e == 3:
    vf = v
    print('Duas parcelas de R$ {:.2f}'.format(v / 2))
elif e == 4:
    vf = v * 1.2
    ee = int(input('Digite o número de parcelas desejado: '))
    print('Você escolheu pagar {}x parcelas de R$ {:.2f}'.format(ee, vf / ee))

else:
    print('Opção inválida!')
print('O valor inicial do produto era R$ {:.2f} e o valor final será R$ {:.2f}'.format(v, vf))
