#Funcao de velocidade média
def vel_media(espaco,tempo):
    vel_media = espaco/tempo
    print(f'Velocidade média: {vel_media } m/s')
vel_media(100,20)

#PARAMETROS PARA FUNCAO
#Funcao com parametro opcional
def dados_pessoais(nome, idade=None):
    print(f'Seu nome é {nome}')
    if idade is not None:
        print(f'Sua idade é {idade}')
    else:
        print('Idade nao informada')
dados_pessoais('Matheus') #Nome é o parametro obrigatorio para nossa func
dados_pessoais('Matheus', 25)
dados_pessoais(20) #Python obedece ordem dos parametro, logo nome = 20
#dados_pessoais(idade=20) #Para poder passar a idade

#FUNCAO COM RETORNO
#Utilizar funcao vel_media para calcular a aceleracao
def vel_media_return(espaco,tempo):
    vel_media = espaco/tempo
    return vel_media
aceleracao = vel_media_return(100,20)/20
print(aceleracao)

#FUNCAO COM MULTIPLOS RETORNOS
def calculadora(x,y):
    return {'soma':x+y,'subtracao':x-y} #Retorna um dicionario
resultados = calculadora(1,2) 
for key in resultados:
    print(f'{key}:{resultados[key]}')


#NUMEROS ARBITRÁRIOS DE PARÂMETROS(*ARGS)
#Variáveis mágicas: *args e**kwargs que permitem passar um num variável de argumentos
# *Args é geralmente usado qdo nao sabemos qtos arg tem a nossa funcao
# o "*" executa um empacotamento de dados para facilitar passagem de dados
# e a funcao, ao receber esse empacotamento de dados, desempacota
def teste(arg, *args):
    print(f'Primeiro argumento {arg}')
    for arg in args:
        print(f'Outro argumento {arg}')
lista = ['é', 'muito', 'legal']
teste('python', *lista)

# NUMEROS ARBITRÁRIO DE CHAVES (*KWARGS)
# Usado para manipular arg nomeados em uma funcao
def minha_funcao(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} = {value}')
minha_funcao(nome='Dona Hilda')
dicionario = {'nome':'Joao','idade':25}
minha_funcao(**dicionario)

# CONCLUINDO: *AEGS ESPERA UMA TUPLA DE ARGUMENTOS POSICIONAIS,
# JÁ **KWARGS ESPERA UM DIC COM ARGUMENTOS NOMEADOS

