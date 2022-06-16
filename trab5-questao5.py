M = []
TURMA = []
dado = []
media = 0
for turmas in range(1, 3):
    print(f'======== {turmas}ª TURMA ========')
    for alunos in range(1, 4):
        print(f'---- {alunos}° ALUNO ----')
        dado.append(float(input('1ª nota: ')))
        dado.append(float(input('2ª nota: ')))
        dado.append((dado[-1] + dado[-2]) / 2)
        M.append(dado)
        dado = []
for c in range(0, 3):
    media += M[c][2]
TURMA.append(media / 3)
media = 0
for c in range(3, 6):
    media += M[c][2]
TURMA.append(media / 3)
print('-=' * 10)
if TURMA[0] > TURMA[1]:
    print(f'A turma 1 tem a maior média, com {TURMA[0]:.1f}')
elif TURMA[0] < TURMA[1]:
    print(f'A turma 2 tem a maior média, com {TURMA[1]:.1f}')
elif TURMA[0] == TURMA[1]:
    print(f'As duas turmas tem a mesma média, com {TURMA[0]:.1f}')
print('-=' * 10)
print(TURMA)
print(M)
for c in range(0, 2):
    if c == 0:
        ini = 0
        fim = 3
    else:
        ini = 3
        fim = 6
    a = 1
    for c2 in range(ini, fim):
        if M[c2][2] > TURMA[c]:
            print(f'O aluno {a} da turma {c + 1} tem a média maior que a de sua turma, com {M[c2][2]:.1f}.')
        a += 1