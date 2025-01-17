# MAIOR E MENOR VALOR

dec = 'S'
cont = soma = maior = menor = 0

while dec != 'N':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    dec = str(input('Quer continuar [S/N]: ')).upper()
print(f'Você digitou {cont} números e a média foi {soma / cont:.2f}.')
print(f'O maior valor foi {maior} é o menor foi {menor}.')
