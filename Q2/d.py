import numpy as np
import statsmodels.api as st
from statsmodels.sandbox.regression.predstd import wls_prediction_std

tamanho = [128, 256, 384, 512, 640, 768, 896, 1024]
obs2 = [375, 850, 1644, 3123, 6839, 14567, 27439, 52129]

a = np.array(tamanho)
b = np.array(obs2)

const = st.add_constant(a)

modelo = st.OLS(b, const)

resultado = modelo.fit()

inter1, inter2 = resultado.conf_int(alpha=0.1)

print(inter1, inter2)