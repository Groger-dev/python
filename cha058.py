#Melhore o jogo do desafio 028 onde o PC "pensa" em um número entre 0 e 10. Só que dessa vez o jogador vai adivinhar até acertar.
#No final o programa deve mostrar quantos palpites foram necessários para acertar o número.
from random import randint
from time import sleep
print('Estou pensando em um número entre 0 e 10...')
pc = randint(0,10)
sleep(3)
print('Pronto! tenta adivinhar')
user = int(input('Digite o seu palpite: '))
tentativas = 1
while user != pc:
    user = int(input('Você errou! Tente novamente: '))
    tentativas +=1
if tentativas == 1:
    print('Você acertou na primeira tentativa! Muito beeeeem!')
elif tentativas <= 5:
    print('Nada mal, você acertou rápido!')
elif tentativas < 10:
    print('Eita, dá pra melhorar na próxima vez hehehe')
else:
    print('Quase que não vai hehehehe!')
print('Você precisou de {} tentativa(s) para acertar'.format(tentativas))
