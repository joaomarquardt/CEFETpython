'''2a Questão: Faça um programa que leia uma frase e uma palavra e em seguida determine o número de vezes que a palavra
aparece na frase. Exemplo: Frase:  Ana e Mariana gostam de banana. Palavra: ana Temos que a palavra ana ocorre 4 vezes
na frase. Obs.: Seu programa não deve diferenciar letras minúsculas de maiúsculas. '''

fraseEscolhida = str.lower(input("Digite uma frase.\n"))

fraseEscolhida = fraseEscolhida.split(" ")
fraseEscolhida = "".join(fraseEscolhida)

palavra = str.lower(input("Digite uma palavra para encontrar.\n"))
palavra = palavra.split(" ")
palavra = "".join(palavra)
resposta = 0

while len(fraseEscolhida) > 0:

    if fraseEscolhida[:len(palavra)] == palavra:
        resposta = resposta + 1
    fraseEscolhida = fraseEscolhida[1:len(fraseEscolhida)]

if resposta == 1:
    print("A palavra foi encontrada", resposta, "vez na frase.")
elif resposta > 1:
    print("A palavra foi encontrada", resposta, "vezes na frase.")
elif resposta == 0:
    print("A palavra", palavra, "não foi encontrada na frase.")
print('\nAcabou cambada!')
