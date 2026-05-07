#analysing string

nome = input('Digite um nome: ').strip()
print('Analisando o nome...')
print('Maiúsculo: {}'.format(nome.upper()))
print('Minúsculo: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e possui {} letras'.format(separa[0], len(separa[0])))
