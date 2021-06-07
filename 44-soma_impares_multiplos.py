# calcular a soma entre todos os numeros ímpares que são multiplos de 3 e que se encontrem no intervalo de 1 até 500

soma = 0
cont = 0
for c in range(1, 501, 2):
   if c%3 == 0:
       soma += c
       cont += 1
print('A soma dos {} valores solicitados é: {}' .format(cont, soma))





