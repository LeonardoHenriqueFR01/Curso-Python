# Valores únicos em uma lista

valores = []  # Lista vazia

while True:
    valor = int(input('Digite um valor: '))  # Solicitando um valor

    # Verificando se o valor já está na lista
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não será adicionado à lista.')

    # Verificando se o usuário deseja continuar
    while True:
        escolha = input('Deseja continuar? [Y/N]: ').strip().upper()
        if escolha in ['Y', 'N']:
            break
        else:
            print('Entrada inválida! Digite apenas Y ou N.')

    # Encerrando o programa caso o usuário escolha 'N'
    if escolha == 'N':
        print('-=' * 30)
        print(f'Você adicionou os valores {sorted(valores)}')  # Exibindo os valores ordenados
        break
