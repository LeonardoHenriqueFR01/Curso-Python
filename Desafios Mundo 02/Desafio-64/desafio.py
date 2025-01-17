# TRATANDO VARIOS VALORES 

valor = int(input('Digite um número [999 para parar]: '))
cont = 0
soma = 0

while valor != 999:
    cont += 1
    soma += valor
    valor = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
