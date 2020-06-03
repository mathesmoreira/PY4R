import re

horario_inicio = input('Digite o horário de início: ')
horario_final = input('Digite o horário final: ')

div_horario_inicio = []
div_horario_final = []
div_horario_inicio = re.findall('[0-9][0-9]',horario_inicio)
div_horario_final = re.findall('[0-9][0-9]',horario_final)

hora_inicio = int(div_horario_inicio[0])
hora_final = int(div_horario_final[0])
minuto_inicio = int(div_horario_inicio[1])
minuto_final = int(div_horario_final[1])
segundo_inicio = int(div_horario_inicio[2])
segundo_final = int(div_horario_final[2])

hora_fim = hora_final - hora_inicio
if hora_inicio == hora_final:
    minuto_fim = minuto_final - minuto_inicio
elif (hora_final - hora_inicio) == 1:
    minuto_fim = (59 - minuto_inicio) + minuto_final

segundo_fim = (60 - segundo_inicio) + segundo_final

print(f'Resultado: Horas {hora_fim}, minutos{minuto_fim} e segundos{segundo_fim}')