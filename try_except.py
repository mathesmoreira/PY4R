# Testando Try e Except

n = 1
while n == 1:
    print('Digite Done para finalizar o processo')
    numero = input("Digite um NUMERO: ")
    try:
        num = int(numero)
    except:
        num = -1
    if numero == 'Done':
        break

    if num > 0:
        print("Boa, voce digitou um numero")
        n = n + 1
    else:
        print("Voce NAO digitou um numero!")
        resp = input("Voce quer tentar novamente? (Y/N)")
        if resp == 'Y':
            n = 1
        elif resp == 'N':
            print("Tenha um bom dia")
        else:
            print("Desculpe mas nao pude entender sua resposta")
