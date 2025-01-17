# Tabuada v3

while True:
    num = int(input('Digite o número da tabuada: '))
    if num <= 0:
        print('FIM')
        break

    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
