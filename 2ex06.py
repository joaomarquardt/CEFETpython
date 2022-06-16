#6) Faça um programa que leia um caractere alfanumérico e diga se ele é uma vogal.
n = str(input('Digite um caractere alfanumérico: ')).strip().lower()
if n.isalnum() == False:
    print(f"O caractere '{n}' não é alfanumérico")
else:
    if n in 'aeiou':
        print(f'O caractere {n} é uma vogal')
    else:
        print(f'O caractere {n} não é uma vogal')