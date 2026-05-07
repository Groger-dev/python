#Quantos litros de tinta eu preciso para pintar essa parede?
#1L = 2m²

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

tinta = (altura * largura) / 2

print('Você precisará de {:.3f} litro(s) de tinta.'.format(tinta))
