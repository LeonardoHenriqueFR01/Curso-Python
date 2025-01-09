# Calculando desconto

produto = float(input('Qual é o preço do produto: R$'))

desconto = produto - (produto / 100 * 5) 

print(f'O produto que custava R${produto}, na promoção com desconto de 5% vai custar R${desconto:.2f}')
