import pandas as pd
import numpy as np
import random

#Data Frame

df=pd.DataFrame({'id':[i for i in range(1,11)],
                 'Marks':[23,24,24,np.nan,12,24,np.nan,34,24,57],
                 'Grade':['B','C','A',np.nan,'A','C','D',np.nan,'A','F'],
                 'Gender':[random.choice(['M','F']) for i in range (1,11)]})

#One Hot Encoding on the Gender column

df['Male']=np.where(df['Gender']=='M',1,0)
df['Female']=np.where(df['Gender']=='F',1,0)
df=df.drop(columns=['Gender'])

print(df)