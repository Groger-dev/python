#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre o seu status:
#Abaixo de 18.5 - Abaixo do peso
#Entre 18.5 e 25 - Peso ideal
#25 até 30 - Sobrepeso
#30 até 40 - Obesidade
#Acima de 40 - obesidade mórbida

a = float(input('Insert your height in metres: '))
m = float(input('Insert your weight in kilograms: '))
imc = m / (a * a)

if imc < 18.5:
    print('Seu IMC deu {:.2f}, isso significa ABAIXO do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC deu {:.2f}, isso significa que você está com seu peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC deu {:.2f}, isso significa que você está ACIMA do peso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC deu {:.2f}, isso significa OBESIDADE'.format(imc))
else:
    print('Seu IMC deu {:.2f}, cuidado você está com OBESIDADE MÓRBIDA'.format(imc))
