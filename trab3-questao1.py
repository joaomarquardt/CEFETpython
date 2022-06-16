'''1a Questão: Faça um programa para conjugar verbos regulares (terminados em ar, er e ir), no presente, pretérito perfeito
e no futuro do presente. O usuário deve entrar com o verbo no infinitivo pessoal (ex.: amar, beber, partir, etc.).
O programa deve verificar se o verbo está no infinitivo, se não estiver deve mandar a mensagem:
“O verbo deve estar no infinitivo”, e pedir para o usuário entrar novamente com o verbo. Seu programa deve ler o verbo,
mostrar as conjugações nas 3 pessoas do singular e nas 3 pessoas do plural, incluindo os pronomes pessoais
(eu, tu, ele, nós, vós, eles). O programa deve terminar quando for digitado a palavra “FIM”.
'''
from time import sleep
print('-=' * 20,
      f'\n{"CONJUGADOR DE VERBOS REGULARES":^40}')
print('-=' * 20, '\n')
while True:
    while True:
        verbo = str(input('Digite um verbo regular [FIM para parar]: ')).lower().strip()
        if verbo[-1] == 'r' and verbo[-2] in 'aeiou' or verbo == 'fim':
            break
        else:
            print('O verbo deve estar no infinitivo.')
    if verbo == 'fim':
        break
    print('CONJUGANDO...')
    sleep(1)
    aux = aux2 = ''
    if verbo[-2] == 'a':
        aux = 'a'
    elif verbo[-2] == 'e':
        aux = 'e'
    elif verbo[-2] == 'i':
        aux = 'i'
    print('--' * 20)

    print(f"VERBO '{verbo.upper()}' NO PRESENTE")
    print(f'\nEU: {verbo[:-2]}' + 'o')
    if aux == 'a':
        print(f'TU: {verbo[:-2]}' + 'as')
        print(f'ELE: {verbo[:-2]}' + 'a')
    else:
        print(f'TU: {verbo[:-2]}' + 'es')
        print(f'ELE: {verbo[:-2]}' + 'e')
    print(f'NÓS: {verbo[:-2]}' + aux + 'mos')
    if aux == 'a':
        aux2 = 'a'
    elif aux == 'e':
        aux2 = 'e'
    print(f'VÓS: {verbo[:-2]}' + aux2 + 'is')
    print(f'ELES: {verbo[:-2]}', end='')
    print('am' if aux == 'a' else 'em')
    print('--' * 20)

    print(f"VERBO '{verbo.upper()}' NO PRETÉRITO PERFEITO")
    print(f'\nEU: {verbo[:-2]}', end='')
    print('ei' if aux == 'a' else 'i')
    print(f'TU: {verbo[:-2]}' + aux + 'ste',
    f'\nELE: {verbo[:-2]}', end='')
    print('ou' if aux == 'a' else aux + 'u')
    print(f'NÓS: {verbo[:-2]}' + aux + 'mos',
    f'\nVÓS: {verbo[:-2]}' + aux + 'stes',
    f'\nELES: {verbo[:-2]}' + aux + 'ram')
    print('--' * 20)
    print(f"VERBO '{verbo.upper()}' NO FUTURO DO PRESENTE"
    f'\n\nEU: {verbo[:-2]}' + aux + 'rei',
    f'\nTU: {verbo[:-2]}' + aux + 'rás',
    f'\nELE: {verbo[:-2]}' + aux + 'rá',
    f'\nNÓS: {verbo[:-2]}' + aux + 'remos',
    f'\nVÓS: {verbo[:-2]}' + aux + 'reis',
    f'\nELES: {verbo[:-2]}' + aux + 'rão')
    print('--' * 20)
print('Até mais! :)')