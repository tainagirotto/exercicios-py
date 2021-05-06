#Ler o nome de uma cidade e falar se ela começa ou não com o nome "santo"

city = input('Digite o nome da sua cidade: ').strip()
print(city[:5].lower() == 'santo')

