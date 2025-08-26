#########################################################
#              Calculadora De Matrizes 3.0              #
#########################################################


def criar_matriz(nome):
    print(f"\n--- Criando a matriz {nome} ---")
    linhas = int(input("Número de linhas: "))
    colunas = int(input("Número de colunas: "))
    mi = int(input("Multiplicador para i: "))
    ei = int(input("Expoente para i: "))
    mj = int(input("Multiplicador para j: "))
    ej = int(input("Expoente para j: "))

    matriz = [[mi * (i+1)**ei + mj * (j+1)**ej for j in range(colunas)] for i in range(linhas)]
    return matriz


def exibir_matriz(matriz, titulo="Matriz"):
    print("\n" + titulo)
    print("=" * (len(matriz[0]) * 4 + 3))
    for linha in matriz:
        print("| " + "  ".join(f"{x}" for x in linha) + " |")
    print("=" * (len(matriz[0]) * 4 + 3))


def soma_matrizes(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def subtrai_matrizes(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiplica_matrizes(a, b):
    linhas_a, colunas_a = len(a), len(a[0])
    linhas_b, colunas_b = len(b), len(b[0])

    if colunas_a != linhas_b:
        return None  # Multiplicação impossível

    resultado = [[0] * colunas_b for _ in range(linhas_a)]
    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                resultado[i][j] += a[i][k] * b[k][j]
    return resultado


# Programa principal
A = criar_matriz("A")
B = criar_matriz("B")

exibir_matriz(A, "Matriz A")
exibir_matriz(B, "Matriz B")

mesmo_tamanho = (len(A) == len(B) and len(A[0]) == len(B[0]))

print("\n--- Operações disponíveis ---")
opcoes = []
if mesmo_tamanho:
    print("1 - Soma (A + B)")
    print("2 - Subtração (A - B)")
    opcoes.extend([1, 2])

if len(A[0]) == len(B):  # Condição para multiplicação
    print("3 - Multiplicação (A x B)")
    opcoes.append(3)

if not opcoes:
    print("⚠️ Nenhuma operação possível entre essas matrizes.")

else:
    escolha = int(input("\nEscolha a operação: "))
    if escolha == 1:
        resultado = soma_matrizes(A, B)
        exibir_matriz(resultado, "Resultado da Soma (A + B)")
    elif escolha == 2:
        resultado = subtrai_matrizes(A, B)
        exibir_matriz(resultado, "Resultado da Subtração (A - B)")
    elif escolha == 3:
        resultado = multiplica_matrizes(A, B)
        if resultado:
            exibir_matriz(resultado, "Resultado da Multiplicação (A x B)")
        else:
            print("⚠️ Multiplicação impossível.")