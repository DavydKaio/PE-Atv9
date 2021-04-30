from scipy import stats

numero_palavras_chaves = [1,2,4,8,16]
tempo_decorrido = [0.75,0.70,0.80,1.28,1.60]

n = len(numero_palavras_chaves)

def calcular_M(n, x, y):
    sum_xy = []

    for i in range(len(x)):
        sum_xy.append(x[i] * y[i])

    x_quadrado = []
    for i in range(len(x)):
        x_quadrado.append(x[i] ** 2)

    numerador = n * sum(sum_xy) - sum(x) * sum(y)
    denominador = n * sum(x_quadrado) - (sum(x)) ** 2

    m = numerador / denominador

    return m


def calcular_B(n, x, y):
    m = calcular_M(n, numero_palavras_chaves, tempo_decorrido)   

    parte1 = sum(y) / n
    parte2 = m * (sum(x) / n)

    b = parte1 - parte2

    return b 


print(calcular_M(n, numero_palavras_chaves, tempo_decorrido))
print(calcular_B(n, numero_palavras_chaves, tempo_decorrido))
