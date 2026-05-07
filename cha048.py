#Faça um programa que calcule a soma de todos os números ímpares que são múltiplos de 3 no intervalo de 1 a 500
soma = 0
for num in range(1, 501):
    if num % 3 == 0:
        soma += num
print(soma)
