melhorVolta = tempoMelhor = 0
melhorVoltista = ''
matriz = []
dado = []
media = 0
for c in range(1, 3):
    volta = 0
    nome = str(input(f'Nome do {c}° corredor: '))
    dado.append(nome)
    for c2 in range(1, 3):
        volta = int(input(f'Tempo da {c2}ª volta: '))
        media += volta
        if c == 1 and c2 == 1:
            tempoMelhor = volta
            melhorVolta = c2
            melhorVoltista = nome
        else:
            print(f'Melhor volta atualmente: {melhorVolta}')
            print(f'Melhor voltista atualmente: {melhorVoltista}')
            print(f'Volta: {volta}')
            print(f'Melhor tempo : {tempoMelhor}')
            if volta < tempoMelhor:
                melhorVolta = c2
                melhorVoltista = nome
    dado.append(media / 2)
    matriz.append(dado)
    dado = []
print(matriz)
print(f'O piloto com a melhor volta foi o {melhorVoltista} na volta {melhorVolta}')
tabela = ['', 0]
for c in range(0, 6):
    if c == 1:
        tabela.append(matriz[c][1])
    '''else:
        while matriz[c][1] not in tabela:
            if matriz[c][1] < tabela[c]:'''
