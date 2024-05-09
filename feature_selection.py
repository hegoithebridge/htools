
import numpy as np
from scipy.stats import chi2_contingency
import pandas as pd


#####################################################################
#
# P-value para dos variables categóricas
#
#####################################################################
def p_value_categoricas(df,var1,var2):
    tabla_frecuencias = pd.crosstab(df[var1], df[var2])

    # Imprimir la tabla de frecuencias cruzadas
    print(tabla_frecuencias)
    # Calcula la estadística chi cuadrado y el valor p
    chi2, p, dof, expected = chi2_contingency(tabla_frecuencias)

    print("Estadística chi cuadrado:", chi2)
    print("Valor p:", p)
    print("Grados de libertad:", dof)


#####################################################################
#
# P-value para una variable numérica con una categórica
#
#####################################################################

from scipy import stats

def p_value_numerica_categorica(df,var_num,var_cat,valor):
    # Datos de los dos grupos
    grupo1 = df[df[var_cat == valor]]
    grupo2 = df[df[var_cat != valor]]


    # Realizar el test t de Student
    t_statistic, p_value = stats.ttest_ind(grupo1, grupo2)

    # Imprimir los resultados
    print("Estadístico t:", t_statistic)
    print("Valor p:", p_value)

    # Interpretación del resultado
    if p_value < 0.05:
        print("Hay una diferencia significativa entre las medias de los dos grupos.")
    else:
        print("No hay suficiente evidencia para afirmar que hay una diferencia significativa entre las medias de los dos grupos.")