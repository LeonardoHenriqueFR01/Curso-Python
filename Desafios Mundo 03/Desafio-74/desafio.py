# MAIOR E MENOR NÚMERO SORTEADO 

from random import randint

nums = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]

print(f'Os valores sorteados foram: {nums}')
print(f'O maior valor sorteado foi: {max(nums)}')
print(f'O menor valor sorteado foi: {min(nums)}')
