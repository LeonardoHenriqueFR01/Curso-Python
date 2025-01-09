# Aluguel de carros

km = float(input('Quantidade de Km rodados: '))
dias = int(input('Por quantos dias foi alugado: '))

valor = dias * 60 + km * 0.15

print(f'O total a pagar é de R${valor:.2f}')
