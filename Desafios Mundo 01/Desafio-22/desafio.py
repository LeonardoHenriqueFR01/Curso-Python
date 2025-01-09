# Analisador de textos


nome = str(input('Digite o seu nome: '))

primeiro_nome = nome.split()
nome_sem_espacos = nome.replace(" ", "")

print(f'Seu nome em MAIÚSCULAS é {nome.upper()}')
print(f'Seu nome em MINÚSCULAS é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome_sem_espacos)} letras')
print(f'Seu primeiro nome é {primeiro_nome[0]} e ele tem {len(primeiro_nome[0])} letras')
