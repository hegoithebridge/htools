
from feature_selection import *
import pandas as pd

df = pd.DataFrame({'col_num':[1,2,3,4,5,6,7,8,9],
      'col_num_2':[3,4,5,6,7,8,9,10,11],
      'cat':['no','no','no','no','yes','yes','yes','yes','yes'],
      'cat_2':['a','a','a','a','b','b','b','b','b']})
print(df)
#p_value_numerica_categorica(df,'col_num','cat','yes')
p_value_categoricas(df,'cat','cat_2')