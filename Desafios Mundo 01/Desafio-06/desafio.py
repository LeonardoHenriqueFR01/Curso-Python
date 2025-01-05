# Dobro, Triplo, Raiz quadrada



num = int(input('Digite um número: '))

print(f'O dobro de {num} vale {num * 2}. \nO triplo de {num} vale {num * 3}.')

# Primeira forma de fazer raiz quadrada
print(f'A raiz quadrada de {num} é igual a {num ** 0.5:.2f}.')

# Segunda forma de fazer raiz quadrada usando biblioteca
from math import sqrt
print(f'A raiz quadrada de {num} é igual a {sqrt(num):.2f}.')
