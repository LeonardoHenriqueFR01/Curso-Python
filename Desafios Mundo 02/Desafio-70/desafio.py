# Estatísticas em produtos 


total = tot_mil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    resp = str(input('Quer continuar [S/N]: ')).upper()
    if preço > 1000:
        tot_mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    if resp == 'S':
        continue
    elif resp == 'N':
        print(f'O total da compra foi R${total:.2f}')
        print(f'Temos {tot_mil} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
        break
