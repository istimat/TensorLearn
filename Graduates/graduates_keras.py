import pandas as pd
import numpy as np
import copy
#%matplotlib inline

df_graduates = pd.read_csv('graduates_raw.csv')
print(df_graduates.head())
print(df_graduates.info())
df_graduates.boxplot('Sexe','Ani',rot = 30,figsize=(5,6))