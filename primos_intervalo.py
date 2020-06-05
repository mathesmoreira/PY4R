# Programa para saber e dizer quais são os primos em um intervalo pré-digito

# Determinando o intervalo
int_inicio = int(input("Por favor digite o inicio do intervalo: "))
int_fim = int(input("Por favor digite o fim do intervalo: "))

lista_primos = []

# Adicionando um condicional para evitar erro na divisao futura
if int_inicio == 1:
    int_inicio = 3
    lista_primos.append(2)
if int_inicio == 2:
    int_inicio = 3
    lista_primos.append(2)

numero = int_inicio - 1

# Descobrindo os primos no intervalo
while numero > 1 and int_inicio <= int_fim:
    resto = int_inicio % numero
    if resto == 0 and int_inicio <= int_fim:
        int_inicio += 1
        numero = int_inicio - 1
    elif numero == 2 and resto != 0:
        lista_primos.append(int_inicio)
        int_inicio += 1
        numero = int_inicio - 1
    else:
        numero -= 1

print(lista_primos)
