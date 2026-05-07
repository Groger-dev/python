#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada Km/h acimado limite

v = int(input('How fast is the car now? '))
if v > 80:
    print('You have been fined!')
    print('You will receive a fine of ${:.2f} in your house'.format((v - 80) * 7))

print('Dont be so fast, take care!')
