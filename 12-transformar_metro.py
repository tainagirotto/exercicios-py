# Ler um número em metros e mostrar seu valor em cm e mm:

m = float(input('Digite o valor em metros: '))
dm = m * 10
cm = m * 100
mm = m * 1000
km = m/1000
hm = m/100
dam = m/10

print('O valor em cm é {}' .format(cm))
print('O valor em milímetros é {}' .format(mm))
print('O valor em dm é {}' .format(dm))
print('O valor em km é {}' .format(km))
print('O valor em hm {}' .format(hm))
print('O valor em dm {}' .format(dm))
