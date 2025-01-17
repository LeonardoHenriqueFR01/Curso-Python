# Procurando uma string dentro de uma string

nome = str(input('Qual é o seu nome completo: ')).strip()

print(f'Seu nome tem Silva? {"silva" in nome.lower()}')

