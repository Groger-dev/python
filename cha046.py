#Faça um programa que mostre na tela uma contagem refressiva para o estouro de fogos de artifício
#10 a 0 com intervalo de 1seg
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('* Fogos *')

