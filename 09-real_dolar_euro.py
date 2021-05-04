# Mostrar o valor em dólar.

real = float(input('Digite o valor em Real: R$'))

def real_hoje(real):
     dol = real / 5.44
     return dol

def euro_hoje(real):
    euro = real / 6.55
    return euro

print('Você consegue comprar {:.2f} euros' .format(euro_hoje(real)))
print('e {:.2f} dólares' .format(real_hoje(real)))