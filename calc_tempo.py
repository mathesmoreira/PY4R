# Programa calcula o tempo por questao

tempo = input('Digite quanto tempo vc tem para realizar a prova: ')
questoes = input('Digite quantas questoes vc estará respondendo: ')

tempo = float(tempo)
questoes = int(questoes)

tempo_por_questao = tempo / questoes
tempo_total = tempo

for questao in range(questoes):
    print('QUESTAO:', questao + 1, 'Comecar em:', tempo_total)
    tempo_total -= tempo_por_questao
