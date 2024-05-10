
from feature_selection import *
import pandas as pd
import seaborn as sns

df_titanic = sns.load_dataset('titanic')
df_tips = sns.load_dataset('tips')
#print(df_tips.head())
#correlacion_significativa(df_titanic,'fare',0.8)
#test_relacion(df_titanic,'fare',pvalue=0.99)
test_relacion_regression_numeric(df_tips,'tip',0.01)
#print(df_tips.drop('smoker',axis=1).corr())
