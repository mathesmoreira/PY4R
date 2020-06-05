# Funcao que recebe um numero e retorna este, caso digite alguma
# string ele retorna que nao foi digitado um numero

def Isanumber():
    numero = input("Digite um NUMERO:")
    try:
        num = int(numero)
        print(num)
    except ValueError:
        num = -1

    if num > 0:
        print("Boa, voce digitou um numero")
    else:
        print("Voce NAO digitou um numero!")
        resp = input("Voce quer tentar novamente(Y/N)? ")
        if resp == 'Y':
            Isanumber()
        elif resp == 'N':
            print("Tenha um bom dia")
        else:
            print("Desculpe mas nao pude entender sua resposta")


# Chamando a funcao
Isanumber()
