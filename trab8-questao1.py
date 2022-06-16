'''1a Questão: A faculdade de informática de uma universidade possui 2 arquivos referentes aos dados dos candidatos que
fizeram vestibular. O primeiro possui o número de inscrição, o nome do candidato e a renda familiar; o segundo possui a
classificação do candidato, sua matrícula e suas notas nas provas objetivas e discursivas. O primeiro arquivo está
ordenado por número de inscrição e o segundo arquivo está ordenado por classificação. Foi instituído o sistema de cotas
e essa universidade agora precisa destinar 25% de suas vagas aos melhores classificados com renda inferior ou igual a
R$1000,00. Faça um programa que gere dois arquivos de saída, o primeiro contendo os nome, classificação inicial e
classificação final, dos candidatos com renda inferior ou igual a R$1000,00, em ordem de inscrição e o segundo arquivo
contendo os nome, inscrição e classificação inicial dos candidatos que estavam classificados e que perderam a vaga após
a instituição do sistema de cotas. Obs.: Crie o primeiro arquivo mostrado abaixo de forma aleatória. Para criação do
segundo arquivo, gere notas aleatórias para as provas objetivas e discursivas de cada candidato existente no primeiro
arquivo e em seguida ordene a classificação com relação às notas. O critério de ordenação será a média da objetiva com
a discursiva. Se houver empates, o desempate será dado pela maior nota discursiva. '''

'''arqUm.txt: Alunos e renda
arqDois.txt: Classificações

cotistas.txt: Alunos que são cotistas
cotasDesclassificados.txt: Alunos desclassificados. '''

import random

nomeList = ['Marisa', 'Joana', 'Jorge', 'Irineu', 'Fulano', 'Beutrano', 'Ciclana', 'Nunally', 'Ziralda', 'Zoe',
            'Jujuca', 'Toph', 'Ednaldo', 'Nádia', 'Elias', 'Hilda', 'Valmir']
sobrenomeList = ['Mauá', 'Zoinks', 'Lins', 'Silva', 'Kaiba', 'de Abreu', 'Moreira', 'Amane', 'Pirilampo', 'Barra',
                 'la Muerte', 'Feliposo', 'Betanha', 'vi Britannia', 'Gonzales', 'Tiririca']

finalInfo = []
finalNota = []
finalClassi = []


def escArq1(n):
    def sep():
        arquivo.write(str(','))

    arquivo = open('arqUm.txt', 'w')
    for i in range(n):
        insc = str(i + 1)
        insc = ('0' * (5 - len(insc))) + insc
        arquivo.write(str(insc))
        sep()
        arquivo.write(str(random.choice(nomeList)))
        arquivo.write(str(' '))
        arquivo.write(str(random.choice(sobrenomeList)))
        sep()
        arquivo.write(str('R$'))
        arquivo.write(str(random.randint(0, 8000)))
        arquivo.write("\n")
    arquivo.close()


def escArq2(n):
    def sep():
        arquivo.write(str(','))

    arquivo = open('arqDois.txt', 'w')

    for i in range(n):
        insc = str(i + 1)
        insc = ('0' * (5 - len(insc))) + insc
        arquivo.write(str(insc))  # inscrição
        for i in range(2):
            sep()
            nota = (random.randint(0, 1000))  # decimais nao funcionaram, converter depois

            arquivo.write(str(nota))
        arquivo.write("\n")

    arquivo.close()
    arquivo = open('arqDois.txt')
    listaClassi1 = []
    listaClassi2 = []
    listaNota = []

    for i in range(n):
        nota = []
        linhaOr = str(arquivo.readline(-1))
        linha = linhaOr

        # .split dava erro, entao
        for x in range(2):
            if linha[len(linha) - 6:len(linha) - 1] == 1000:  # 1000
                nota.append(1000)
                linha = linha[:len(linha) - 6]
            elif linha[len(linha) - 3] == ',':  # 1 digito
                nota.append(linha[len(linha) - 2])
                linha = linha[:len(linha) - 3]
            elif linha[len(linha) - 4] == ',':  # 2 digitos
                nota.append(linha[len(linha) - 3:len(linha) - 1])
                linha = linha[:len(linha) - 4]
            else:
                nota.append(linha[len(linha) - 4:len(linha) - 1])
                linha = linha[:len(linha) - 5]  # 3 digitos
            linha = linha + '\n'

        media = (int(nota[0]) * 10) + (int(nota[1]) * 10)
        media = media // 2

        listaClassi1.append(linhaOr)
        listaClassi2.append(media)
        listaNota.append(nota[0])

    finalClassi = []
    finalClassi = listaClassi2.copy()
    finalClassi.sort(reverse=True)
    finalInfo = []
    finalNota = []

    for i in range(n):
        aux = listaClassi2.index(finalClassi[i])
        finalInfo.append(listaClassi1[aux])
        finalNota.append(listaNota[aux])

    for i in range(n):  # condição de empate
        if i < n - 1:
            if finalClassi[i] == finalClassi[i + 1]:
                if finalNota[i] < finalNota[i + 1]:
                    finalInfo.insert(i, finalInfo[i + 1])
                    finalInfo.pop(i + 2)
                    finalNota.insert(i, finalInfo[i + 1])
                    finalNota.pop(i + 2)

    arquivo.close()
    arquivo = open('arqDois.txt', 'w')

    for i in range(n):
        zero = str(i + 1)
        zero = ('0' * (6 - len(zero))) + zero
        arquivo.write(str(zero))
        sep()
        arquivo.write(str(finalInfo[i]))

    arquivo.close()


cotaAlunos = []


def cotas(alunostotal, vagas):
    def sep():
        arquivo.write(str(','))

    arquivo = open('arqUm.txt', "r")
    arquivo1 = open('arqDois.txt', "r")

    arq1list = []
    arq2lista = []
    linhaInsc = []

    for i in range(alunostotal):
        linhaOr = arquivo.readline(-1)
        arq1list.append(linhaOr)
        linhaOr1 = arquivo1.readline(-1)
        arq2lista.append(linhaOr1)
        linha = linhaOr
        if '$' in linha[len(linha) - 5:len(linha) - 1]:
            cotaAlunos.append(linhaOr)
        elif linha[len(linha) - 5:len(linha) - 1] == '1000':
            cotaAlunos.append(linhaOr)
            linha = linha[:len(linha) - 8]

        # extrai inscrições
        linhaInsc2 = arq2lista[i]
        linhaInsc2 = linhaInsc2[7:12]
        linhaInsc.append(linhaInsc2)

    linhaCota = cotaAlunos.copy()
    classiCotaOr = []

    for i in range(len(cotaAlunos)):  # extrai nomes
        linhaOr = linhaCota[i]
        linha = linhaOr
        if linha[len(linha) - 3] == '$':  # 1 digito
            linha = linha[:len(linha) - 5]
        elif linha[len(linha) - 4] == '$':  # 2 digitos
            linha = linha[:len(linha) - 6]
        else:
            linha = linha[:len(linha) - 7]  # 3 digitos

        linha = linha[6:]
        linhaCota.insert(i, linha)
        linhaCota.pop(i + 1)

        # extrai classificação original
        a = 0
        while True:
            if linhaInsc[a] == linhaOr[:5]:
                insc = arq2lista[a]
                insc = insc[:6]
                classiCotaOr.append(insc)

                break
            a = a + 1

    # classificação nova dos melhores cotistas
    classiCotaNo = []
    classiCotaNo = classiCotaOr.copy()
    faltam = vagas // 4

    copiaCla = classiCotaNo.copy()
    copiaCla.sort()

    novolist = []

    for i in range(len(cotaAlunos)):
        if int(classiCotaNo[i]) <= (vagas - faltam):
            faltam -= 1

            a = copiaCla.index(classiCotaNo[i])
            copiaCla.pop(a)

    if faltam > 0:
        copiaF = faltam

        for i in range(faltam):
            a = 0
            b = 0

            for x in range(len(cotaAlunos)):
                b += 1

                if int(classiCotaNo[x]) == (vagas - copiaF):
                    a = 1
                    if len(copiaCla) > 0:
                        copiaCla.pop(x)
                    b -= 1

            if not a == 1:
                novo = str(vagas - copiaF)
                novo = ('0' * (5 - len(novo))) + novo
                new = classiCotaNo.index(copiaCla[1])
                classiCotaNo[new] = novo
                copiaCla.pop(0)

                novolist.append(novo)

                copiaCla.pop(0)

            copiaF -= 1

    nome = []
    inDes = []

    arquivo.close()
    arquivo1.close()
    arquivo = open('cotistas.txt', 'w')

    for i in range(len(cotaAlunos)):
        arquivo.write(linhaCota[i])
        sep()
        arquivo.write(classiCotaOr[i])
        sep()
        arquivo.write(str(classiCotaNo[i]))
        arquivo.write('\n')

    arquivo.close()
    arquivo = open('cotasDesclassificados.txt', 'w')

    for i in range(len(nome)):
        arquivo.write(nome[i])
        sep()
        arquivo.write(inDes[i])
        sep()
        arquivo.write(novolist[i])

    arquivo.close()


escArq1(50)
escArq2(50)
cotas(50, 16)  # numero de alunos, não funcionou tentando descobrir sozinho