#7) Faça um programa que leia um caractere alfanumérico e diga se ele é consoante, número ou vogal.
n = str(input('Digite um caractere alfanumérico: ')).strip().lower()
if n.isalnum() == False:
    print(f"O caractere '{n}' não é alfanumérico")
else:
    if n.isnumeric() == True:
        print(f'O caractere {n} é númérico')
    elif n.isalpha() == True:
        if n in 'aeiou':
            print(f'O caractere {n} é uma vogal')
        else:
            print(f'O caractere {n} é uma consoante')