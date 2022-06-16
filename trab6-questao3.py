trabalho = ( 'Lavar', 15,'Cozinhar', 60, 'Dobrar roupa', 60, 'Aspirar', 45, 'Ver dispensa', 10, 'Estender roupa', 25)
aux = 0
print(f'\033[36m{" Assistente da Casa ":=^40}\033[m\n')
print('Seu assistente na rotina de manter a casa.')
print('-+' * 14, '\n Lista de Afazeres\n', '-+' * 14)
for c in range(0, 6):
    print(f'{trabalho[aux]:.<30}', end=' ')
    aux += 1
    print(f'\033[33m{trabalho[aux]} minutos\033[m')
    aux += 1

while True:
    tarefa = [str(input('Qual a primeira tarefa realizada? ')).capitalize().strip()]
    print('As tarefas ditas até agora são -')
    print(tarefa)
    
    if tarefa[0] in trabalho:
        while True:
            aux = str(input('Mais alguma tarefa foi realizada?(Digite N para parar)')).capitalize().strip()
            if aux in 'Nn':
                break
            elif tarefa not in trabalho:
                print('As tarefas ditas até agora são - ')
            tarefa.append(aux)
            print(tarefa)
    else:
        print('Uma dessas tarefas não foi digitada corretamente ou não tem informações nessa aplicação.')
        tarefa = str(input('Qual a primeira tarefa realizada? ')).capitalize().strip()
        
    while True:
        listtemp = []
        
        opcao = str(input('Você gostaria de saber: Tarefas faltando | Tempo\n')).upper().strip()
        if opcao == 'TEMPO':
            aux = 1
            aux3 = 0
            for x in range(6):
                listtemp.append(trabalho[aux])
                aux += 2
            aux = 0
            aux2 = sum(listtemp)
            for x in range(len(tarefa)):
                aux3 = trabalho.index(tarefa[aux]) + 1
                aux2 -= trabalho[aux3]
                aux += 1
            print(f'O tempo das tarefas à realizar é de {aux2} minutos.\nVocê consegue!\n')
        elif opcao == 'TAREFAS FALTANDO':
            aux = 0
            aux3 = 0
            for x in range(6):
                listtemp.append(trabalho[aux])
                aux += 2
            for element in listtemp:
                if element in tarefa:
                    listtemp.remove(element)
            print(listtemp)
            print('As tarefas que faltam são:\n','-+' * 14)
            for x in listtemp:
                print(x)
        
        continuar = str(input('Deseja realizar outra função? [S/N] ')).strip()[0]
        if continuar in 'Nn':
            break
    continuar = str(input('Deseja falar novamente as tarefas realizadas? [S/N] ')).lower().strip()[0]
    if continuar == 'n':
        break
