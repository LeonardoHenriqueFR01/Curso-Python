# Primeira e última ocorrência de uma string

frase = str(input('Digite uma frase: ')).upper()

print(f'A letra (A) aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra (A) aparace na posição {frase.find("A")}.')
print(f'A última letra (A) apareceu na posição {frase.rfind("A") + 1}.')
