def multiplicar_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    matriz_resultante = []
    for l in range(filas_matriz1):
        fila = [0] * columnas_matriz2
        matriz_resultante.append(fila)

    # Verificar si las matrices se pueden multiplicar
    if columnas_matriz1 == filas_matriz2:
        for i in range(filas_matriz1):
            for j in range(columnas_matriz2):
                for k in range(filas_matriz2):
                    matriz_resultante[i][j] += matriz1[i][k] * matriz2[k][j]

    return matriz_resultante

def traspuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    traspuesta_matriz = []
    for l in range(columnas):
        fila = [0] * filas
        traspuesta_matriz.append(fila)

    for i in range(filas):
        for j in range(columnas):
            traspuesta_matriz[j][i] = matriz[i][j]

    return traspuesta_matriz

def multiplicar_matriz_por_escalar(matriz, escalar):
    resultado = []
    for fila in matriz:
        fila_resultado = []
        for elemento in fila:
            fila_resultado.append(elemento*escalar)
        resultado.append(fila_resultado)
    return resultado


def resta_matrices(matriz1, matriz2):
    resultado=[]
    if len(matriz1) != len(matriz2) or len(matriz1[0]) == len(matriz2[0]):
        for i in range(len(matriz1)):
            fila = []
            for j in range(len(matriz1[0])):
                fila.append(matriz1[i][j] - matriz2[i][j])
            resultado.append(fila)

    return resultado

def gradiente(A,x,b):
    tras = traspuesta(A)
    multpor2 = multiplicar_matriz_por_escalar(tras,2)
    multA = multiplicar_matrices(multpor2,A)
    mult = multiplicar_matrices(multA,x)

    mult2 = multiplicar_matrices(multpor2,b)

    return resta_matrices(mult, mult2)

def moduloVector(vector):
    sol = 0
    for i in vector:
        sol = sol + pow(i[0],2)
    return pow(sol,1/2)

def descensoGradiente(A,b,x_0,alpha,epsilon):
    x = x_0
    g = gradiente(A,x,b)
    while (moduloVector(g) > epsilon):
        x = resta_matrices(x,multiplicar_matriz_por_escalar(g, alpha))
        g = gradiente(A,x,b)
    return x



def casodeprueba():
    try:
        xy = list(map(int, input().split()))
        ecu = xy[0]
        incog = xy[1]
        A = [None] * ecu
        for i in range(ecu):
            A[i] = list(map(float, input().split()))
        b = [None] * ecu
        aux = list(map(float,input().split()))
        for j in range(ecu):
            b[j] = [aux[j]]
        x_0 = [None] * incog
        aux = list(map(float, input().split()))
        for p in range(incog):
            x_0[p] = [aux[p]]
        alpha = float(input())
        epsilon = float(input())

        if(alpha > 0 and epsilon > 0):
            solucion = descensoGradiente(A,b,x_0,alpha,epsilon)
            for p in solucion:
                print('%.4f'% p[0], end=' ')
            print()
            return True
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    while casodeprueba():
        pass