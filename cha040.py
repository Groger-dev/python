#Crie um programa que leia duas notas de um aluno sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Entre 5.0 e 6.9: RECUPERAÇÃO
#Superior ou igual a 7.0: APROVADO
n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite uma outra nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m < 5.0:
    print('\33[1;31mREPROVADO!\33[m Estude bastante para a RECUPERAÇÃO!')
elif m >= 5.0 and m <= 6.9:
    print('É altamente recomendado que você faça a RECUPERAÇÃO para aumentar sua média!')
    print('Pensando melhor você não tem escolha, vou lhe inscrever na recuperação')
else:
    print('Parabéns!!! Você foi \33[1;32mAPROVADO\33[m!')
