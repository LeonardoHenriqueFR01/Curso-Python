# Jogo do par ou impar

from random import randint

print('-=' * 20)
print(f'{"VAMOS JOGAR PAR OU IMPAR":^40}')
print('-=' * 20)

ganhos = 0

while True:
    valor_user = int(input('Digite um valor: '))
    valor_comp = randint(1, 100)
    s = valor_user + valor_comp
    p_i = str(input('Par ou Impar [P/I]: ')).upper()
    print('-' * 40)
    if s % 2 == 0 and p_i == 'P':
        ganhos += 1
        print(f'Você jogou {valor_user} é o computador {valor_comp}. Total {s} é um número PAR')
        print('Vocé ganhou')
        print('-' * 40)
    
    elif s % 2 == 1 and p_i == 'I':
        ganhos += 1
        print(f'Você jogou {valor_user} é o computador {valor_comp}. Total {s} é um número IMPAR')
        print('Você ganhou')
        print('-' * 40)

    elif s % 2 == 0 and p_i != 'P':
        print(f'Você jogou {valor_user} é o computador {valor_comp}. Total {s} é um número PAR')
        print('Você perdeu')
        break
    
    elif s % 2 == 1 and p_i != 'I':
        print(f'Você jogou {valor_user} é o computador {valor_comp}. Total {s} é um número IMPAR')
        print('Você perdeu')
        break

print(f'Vocé teve um total de {ganhos} vezes ganhas!')
