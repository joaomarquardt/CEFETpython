hora = int(input('Horas: '))
minuto = int(input('Minutos: '))
segundo = int(input('Segundos: '))
totalseg = (hora * 60 * 60) + minuto * 60 + segundo
print(f'{hora} hora/s, {minuto} minuto/s e {segundo} segundo/s são {totalseg} segundos')