# Pintando parede

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

litros = (largura * altura) / 2

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {largura * altura}m².')
print(f'Para pintar essa parede, você precisará de {litros}L de tinta.')
