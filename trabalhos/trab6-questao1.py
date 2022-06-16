padaria = ('Pão', 0.50, 'Bala 7 belo', 0.25, 'Torta', 4, 'Bolo', 10, 'Biscoito', 2.50, 'Coxinha', 4,
           'Queijo mussarela', 25.90, 'Queijo prato', 28.90, 'Presunto', 16.45, 'Mortadela', 17.99, 'Salame', 49.90, 'Goiabada', 8,)
comprados = []
aux = conta = qtd = 0
print(f'\033[31m{" PADARIA DOS LINDOS ":=^40}\033[m\n')
print('-=' * 18, '\nVALOR POR UNIDADE')
print('--' * 18)
for c in range(0, 6):
    print(f'{padaria[aux]:.<30}', end=' ')
    aux += 1
    print(f'\033[32mR${padaria[aux]:.2f}\033[m')
    aux += 1
print()
print('-=' * 18, '\nVALOR POR KG')
for c in range(0, 6):
    print(f'{padaria[aux]:.<30}', end=' ')
    aux += 1
    print(f'\033[32mR${padaria[aux]:.2f}\033[m')
    aux += 1
print()
while True:
    produto = str(input('Qual produto você deseja comprar? ')).capitalize().strip()
    while produto not in padaria:
        print('O produto foi digitado errado ou não existe em nosso estoque. Tente novamente.')
        produto = str(input('Qual produto você deseja comprar? ')).capitalize().strip()
    indice = padaria.index(produto) + 1
    valor = padaria[indice]
    if produto in padaria[0:11]:
        qtd = int(input(f'Quantos unidades de {produto.lower()}? '))
        conta += valor * qtd
        valor = valor * qtd
    elif produto in padaria[12:]:
        qtd = int(input(f'Quantos gramas de {produto.lower()}? '))
        valor = valor * (qtd / 1000)
        conta += valor
    comprados += [qtd]
    comprados += [produto]
    comprados += [valor]
    continuar = str(input('Deseja continuar [S/N]? ')).lower().strip()[0]
    if continuar == 'n':
        break
print('\nNOTINHA')
aux = 0
print('--' * 18,
      '\n un / g  |     produto     | valor')
for c in range(len(comprados) // 3):
    print(f'{comprados[aux]:^8}', end='   ')
    aux += 1
    print(f'{comprados[aux]:<17}', end=' ')
    aux += 1
    print(f'R${comprados[aux]:.2f}')
    aux += 1
print('--' * 18)
print(f'\nO valor total foi de R${conta:.2f}')