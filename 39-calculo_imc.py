print('*' * 15, 'CALCULO DE IMC', '*'*15)
nome = input('Qual seu nome? ')
print('Olá, {}! Vamos calcular seu IMC' .format(nome))
altura = float(input('Para isso, digite sua altura: '))
peso = float(input('Agora digite seu peso: '))
imc = peso / (altura ** 2)
print('Seu IMC é de: {:.1f}' .format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está obeso!')
else:
    print('Atenção! Você está com obesidade mórbida!')
