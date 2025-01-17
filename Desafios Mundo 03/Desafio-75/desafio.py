# Análise de dados de uma tupla

t = {1: 'um', 2: 'outro', 3: 'mais um', 4: 'último'}

números = []  # Lista para armazenar os números digitados

for chave in range(1, 5):
    nums = int(input(f'Digite {t[chave]} número: '))
    números.append(nums)  # Adiciona os números na lista

# Contar números iguais
iguais = {num: números.count(num) for num in set(números) if números.count(num) > 1}

# Filtrar números pares
pares = [num for num in números if num % 2 == 0]

# Exibir resultados
print(f'Você digitou os valores: {números}')
print(f'O valor {números[1]} apareceu na 2° posição.')
if iguais:
    print("Números iguais digitados e suas quantidades:")
    for num, qtd in iguais.items():
        print(f'O número {num} foi digitado {qtd} vezes.')
else:
    print("Nenhum número igual foi digitado.")

if pares:
    print(f'Os números pares digitados foram: {pares}')
else:
    print("Nenhum número par foi digitado.")
