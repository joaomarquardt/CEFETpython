alunos = []
notas = []
dado = []
c = 0
while True:
    c += 1
    print(f'===== {c}° ALUNO =====')
    dado.append(str(input('Nome: ')))
    notas.append(float(input('1ª nota: ')))
    notas.append(float(input('2ª nota: ')))
    dado.append(notas[:])
    alunos.append(dado[:])
    notas.clear()
    dado.clear()
    continuar = str(input('Deseja continuar? [S/N] '))[0]
    if continuar in 'Nn':
        break
while True:
    print('N° | NOME          | MÉDIA')
    print('--' * 13)
    for quant in range(0, len(alunos)):
        print(f'{quant} | {alunos[quant][0]:<14} | {(alunos[quant][1][0] + alunos[quant][1][1]) / 2:.2f}')
    print('--' * 13)
    while True:
        mostrarnota = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
        if mostrarnota == 999:
            break
        elif mostrarnota <= len(alunos) - 1:
            print(f'Notas de {alunos[mostrarnota][0]}: {alunos[mostrarnota][1]}')
            print('--' * 13)
        else:
            while True:
                print('Opção inválida. Tente novamente.')
                mostrarnota = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
                if mostrarnota == 999:
                    break
    if mostrarnota == 999:
        break