tabela2020 = ('FLAMENGO', (21, 8, 9, 68, 48, 20, 71), 'INTERNACIONAL', (20, 10, 8, 61, 35, 26, 70), 'ATLÉTICO-MG', (20, 8, 10, 61, 35, 26, 68), 'SÃO PAULO', (18, 12, 8, 59, 41, 18, 66), 'FLUMINENSE', (18, 10, 10, 55, 42, 13, 64), 'GRÊMIO', (14, 17, 7, 53, 40, 13, 59), 'PALMEIRAS', (15, 13, 10, 51, 37, 14, 58), 'SANTOS', (14, 12, 12, 52, 51, 1, 54), 'ATHLETICO-PR', (15, 8, 15, 38, 36, 2, 53), 'BRAGANTINO', (13, 14, 11, 50, 40, 10, 53), 'CEARÁ SC', (14, 10, 14, 54, 41, 3, 52), 'CORINTHIANS', (13, 12, 13, 45, 45, 0, 51), 'ATLÉTICO-GO', (12, 14, 12, 40, 45, -5, 50), 'BAHIA', (12, 8, 18, 48, 59, -11, 44), 'SPORT RECIFE', (12, 6, 20, 31, 50, -19, 42), 'FORTALEZA', (10, 11, 17, 34, 44, -10, 41), 'VASCO DA GAMA', (10, 11, 17, 37, 56, -19, 41), 'GOIÁS', (9, 10, 19, 41, 63, -22, 37), 'Coritiba', (7, 10, 21, 31, 54, -23, 31), 'BOTAFOGO', (5, 12, 21, 32, 62, -30, 27))
aux = aux2 = 0
print('Pos |       Equipe       | Pts')
for c in range(0, 20):
    aux += 1
    print(f'{c + 1:>2}°', f'- {tabela2020[aux2]:<20}', end=' ')
    aux2 += 2
    print(tabela2020[aux][6])
    aux += 1
while True:
    print('-=' * 20)
    time = str(input('Deseja saber as informações de qual time? ')).strip().upper()
    while time not in tabela2020:
        print('O nome do time foi digitado errado ou não consta nos dados. Por favor, tente novamente.')
        time = str(input('Deseja saber as informações de qual time? ')).strip().upper()
    pos = tabela2020.index(time)
    while True:
        opcao = str(input('ESCOLHA UMA DAS OPÇÕES A SEGUIR: VITÓRIAS | EMPATES | DERROTAS | SALDO DE GOLS\n')).upper().strip()
        if opcao == 'VITÓRIAS' or opcao == 'VITORIAS':
            print(f'VIÓRIAS DO {time.upper()}: {tabela2020[pos + 1][0]}')
        if opcao == 'EMPATES':
            print(f'EMPATES DO {time.upper()}: {tabela2020[pos + 1][1]}')
        if opcao == 'DERROTAS':
            print(f'DERROTAS DO {time.upper()}: {tabela2020[pos + 1][2]}')
        if opcao == 'SALDO DE GOLS':
            print(f'SALDO DE GOLS DO {time.upper()}: Fez {tabela2020[pos + 1][3]}, sofreu {tabela2020[pos + 1][4]} e teve um saldo total de {tabela2020[pos + 1][5]} gols')
        continuar = str(input(f'Deseja continuar vendo estatísticas do {time}? [S/N] ')).strip()[0]
        if continuar in 'Nn':
            break
    continuar = str(input(f'Deseja sair do programa? [S/N] ')).strip()[0]
    if continuar in 'Ss':
        break
