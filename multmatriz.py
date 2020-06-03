#Primeiro devemos saber a quantidade de colunas na primeira matriz é igual ao de linhas da segunda
matriz1_colunas = int(input("Digite o número de colunas da sua PRIMEIRA matriz: "))
matriz2_linhas = int(input("Digite o número de linhas da sua SEGUNDA matriz: "))

#Verificando se a multiplicacao entre as matrizes é possível
if matriz1_colunas == matriz2_linhas:
    mult_valida = 1
else:
    print("Multiplicacao não é possível")

#Preenchendo as matrizes 
if mult_valida == 1:
    matriz1_linhas = int(input("Digite a quantidade de linhas da sua PRIMEIRA matriz: "))
    matriz2_colunas = int(input("Digite a quantidade de linhas da sua SEGUNDA matriz: "))
    
    matriz1 = []
    matriz2 = []

    for j in range(matriz1_linhas):
        for i in range(matriz1_colunas):
            matriz1.append(int(input("Digite os termos da PRIMEIRA matriz em linha: ")))

    for j in range(matriz2_linhas):
        for i in range(matriz2_colunas):
            matriz2.append(int(input("Digite os termos da SEGUNDA matriz em coluna: ")))        

    
#Calculando a matriz resultado
    matriz_resultado = []
    termo = 0
    i=0
    j=0
    c=0
    k = 1
    v=0
    linha = 0
    coluna = 0
    l=0

    #CALCULANDO TERMOS DA MATRIZ RESULTADO
    while i < len(matriz1) and j < len(matriz2):
        termo = matriz1[i]*matriz2[j] + termo
        i = i + 1
        j = j + 1
        c = c + 1

        #PULANDO LINHA DA MATRIZ 1 E VOLTANDO A MULTIPLICACAO DE COLUNA EM MATRIZ 2
        if i == k*matriz1_colunas and j == len(matriz2) or i == len(matriz1) and j == len(matriz2): 
            linha = linha + 1
            i = linha*matriz1_colunas

            j=0

        #ADICIONANDO TERMOS À MATRIZ RESULTADO   
        if c == matriz1_colunas and  c == matriz2_linhas:
            matriz_resultado.append(termo)
            termo=0
            c=0
            l=l+1
            coluna = coluna + 1
                
            #PULANDO COLUNA MATRIZ 2
            if coluna == matriz2_colunas:
                j=0
                coluna = 0

            #VOLTANDO A MULT PARA A 1 LINHA DA MATRIZ 1
            if l == matriz2_colunas:
                i = k*matriz1_colunas
                k = k + 1
                l = 0
            else:
                i = linha*matriz1_colunas    
                    
print(matriz_resultado)    