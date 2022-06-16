#16) Faça um programa que leia 2 palavras e diga se elas são iguais ou diferentes.
p1 = str(input('Digite uma palavra: ')).strip().lower()
p2 = str(input('Digite outra palvra: ')).strip().lower()
if p1 == p2:
    print('As duas palavras digitadas são iguais.')
else:
    print(f'As duas palavras digitadas são diferentes.')