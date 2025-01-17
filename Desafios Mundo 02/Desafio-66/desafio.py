# Varios números com flag

valores = 0
soma = 0

while True:
    num = int(input('Digite um número (Digite 999 para parar): '))
    soma += num
    valores += 1
    if num == 999:
        soma -= 999
        valores -= 1
        break
print(f'A soma dos {valores} valores foi {soma}!')
