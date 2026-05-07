#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da viagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas
d = int(input('How far will be your trip?(in Km please) '))

if d <= 200:
    print('Your bus ticket cost ${:.2f}'.format(d * 0.50))
else:
    print('Your bus ticket cost ${:.2f}'.format(d * 0.45))
print('Have a nice trip!')
