#calculadora de aluguel de carros
d = int(input('Digite o número de dias: '))
km = float(input('Digite a distância em km: '))

t = (d * 60) + (km * 0.15)

print('O valor total a ser pago é: R$ {:.2f}'.format(t))
