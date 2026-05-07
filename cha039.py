#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar para o seviço militar
#Se é a hora de se alistar
#Se já passou do tempo para alistamento
#Seu programa tbm deve mostrar quanto já passou, ou ainda falta para o prazo.
from datetime import date
a = date.today().year
print('*' * 25)
print('Alistamento do exército {}'.format(a))
print('*' * 25)
n = int(input('Digite o ano do seu nascimento: '))
i = a - n

if i == 18:
    print('\33[1;32mVocê deve alistar-se neste ano!\33[m')
elif i > 18:
    print('Você está {} ano(s) \33[1;31matrasado\33[m!\n\33[1;31mDirija-se a unidade mais próxima o quanto antes!\33[m'.format(i - 18))
else:
    print('Você ainda não tem idade para se alistar\nEspere até o ano de {}.'.format(n + 18))
