# PORGREÇÃO 


print('Gerador de PA')

primeiro = int(input('primeiro termo: '))
razão = int(input('Razão da PA: '))

termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo} - ', end='')
    termo += razão
    cont += 1
print('FIM')
