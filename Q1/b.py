from math import sqrt
from scipy import stats

numero_palavras_chaves = [1,2,4,8,16]
tempo_decorrido = [0.75,0.70,0.80,1.28,1.60]

n = len(numero_palavras_chaves)

def coef_correlacao(n, x, y):
    sum_xy = []

    for i in range(len(x)):
        sum_xy.append(x[i] * y[i])

    x_quadrado = []
    for i in range(len(x)):
        x_quadrado.append(x[i] ** 2)

    y_quadrado = []
    for i in range(len(y)):
        y_quadrado.append(y[i] ** 2)

    numerador = n * sum(sum_xy) - sum(x) * sum(y)
    denominador = sqrt(n * sum(x_quadrado) - (sum(x)) ** 2) * sqrt(n * sum(y_quadrado) - (sum(y)) ** 2)

    coeficiente = numerador / denominador

    return coeficiente

R_quadrado = coef_correlacao(n, numero_palavras_chaves, tempo_decorrido) ** 2

print(R_quadrado)