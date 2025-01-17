# Maior e menor valores na lista

valores = []  # Lista

# Criando a lista usando loop
for p in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {p}: ')))

maior = max(valores)  # Pegando o maior valor da lista
menor = min(valores)  # Pegando o menor valor da lista

print('-=' * 50)
print(f'Você digitou os valores {valores}')  # Mostrando a lista

# Mostrando o maior valor e suas posições
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, p in enumerate(valores):
    if p == maior:
        print(f'{c}...', end=' ')

# Mostrando o menor valor e suas posições
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for c, p in enumerate(valores):
    if p == menor:
        print(f'{c}...', end=' ')
