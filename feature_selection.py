
import numpy as np
from scipy.stats import chi2_contingency
import pandas as pd
from scipy import stats

import pandas as pd
import numpy as np
from scipy.stats import pearsonr

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, chi2, f_oneway, ttest_ind





def test_relacion_regression_numeric(df, target_col, umbral_corr, pvalue=None):
    # Comprobación de los argumentos de entrada
 #   if not isinstance(df, pd.DataFrame):
 #       print("Error: 'df' debe ser un DataFrame de pandas.")
 #       return None
    
 #   if target_col not in df.columns:
 #       print(f"Error: '{target_col}' no está en las columnas del DataFrame.")
 #       return None
    
 #   if df[target_col].dtype not in [np.float64, np.int64]:
 #       print("Error: 'target_col' debe ser una variable numérica continua o discreta.")
 #       return None
    
 #   if not 0 <= umbral_corr <= 1:
 #       print("Error: 'umbral_corr' debe estar entre 0 y 1.")
 #       return None
    
 #   if pvalue is not None:
 #       if not 0 <= pvalue <= 1:
 #           print("Error: 'pvalue' debe estar entre 0 y 1.")
 #           return None
    
    # Calcular correlación entre 'target_col' y las demás columnas numéricas
    correlaciones = df.select_dtypes(include=[np.number]).corrwith(df[target_col])
    
    # Filtrar por umbral de correlación
    correlaciones_filtradas = correlaciones[abs(correlaciones) > umbral_corr]
    print('Comprobando correlaciones de',target_col,'con:')
    print(correlaciones_filtradas)
    
    # Filtrar por p-value si se proporciona
    if pvalue is not None:
        correlaciones_significativas = []
        for col in correlaciones_filtradas.index:
            _, p_value = pearsonr(df[col], df[target_col])
            if p_value <= 1 - pvalue:
                correlaciones_significativas.append(col)
        return correlaciones_significativas
    else:
        return correlaciones_filtradas.index.tolist()

# Ejemplo de uso
# Suponiendo que df es tu DataFrame y 'target_col' es la columna objetivo
# correlaciones = correlacion_significativa(df, 'target_col', 0.5, pvalue=0.05)
# print(correlaciones)


def test_relacion_regression_categorical(df, target_col, pvalue=0.05):
    # Comprobación de los argumentos de entrada
#    if not isinstance(df, pd.DataFrame):
#        print("Error: 'df' debe ser un DataFrame de pandas.")
#        return None
#    
#    if target_col not in df.columns:
#        print(f"Error: '{target_col}' no está en las columnas del DataFrame.")
#        return None
    
#    if df[target_col].dtype not in [np.float64, np.int64]:
#        print("Error: 'target_col' debe ser una variable numérica continua o discreta.")
#        return None
    
#    if not 0 <= pvalue <= 1:
#        print("Error: 'pvalue' debe estar entre 0 y 1.")
#        return None
    
    # Filtrar columnas categóricas
    columnas_categoricas = df.select_dtypes(include=['object', 'category'])
    
    # Realizar el test de relación para cada columna categórica
    columnas_relacionadas = []
    features = columnas_categoricas.columns
  
    for col in features:
        print('Comparando',target_col,'con',col)
        if target_col == col:
            print('Pasando target col')
            continue
        if df[col].nunique() > 2:  # Si la columna tiene más de dos categorías
            print('Más de dos categóricas')
            test = chi2_contingency(pd.crosstab(df[col].drop(target_col,axis=1), df[target_col]))[1]
            print('chi2:', test)
            if test <= pvalue:
                if target_col!= col:
                    columnas_relacionadas.append(col)
        else:  # Si la columna tiene solo dos categorías
            print('Dos categóricas')
            test = ttest_ind(df[df[col] == df[col].unique()[0]][target_col],
                         df[df[col] == df[col].unique()[1]][target_col])[1]
            print('t-test p-value:',test) 
            if test <= pvalue & target_col != col:
                columnas_relacionadas.append(col)
    
    return columnas_relacionadas

# Ejemplo de uso
# Suponiendo que df es tu DataFrame y 'target_col' es la columna objetivo
# columnas_relacionadas = test_relacion(df, 'target_col')
# print(columnas_relacionadas)