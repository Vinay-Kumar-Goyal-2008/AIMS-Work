import pandas as pd
import numpy as np
import random

#Data Frame

df=pd.DataFrame({'id':[i for i in range(1,11)],
                 'Marks':[23,24,24,np.nan,12,24,np.nan,34,24,57],
                 'Grade':['B','C','A',np.nan,'A','C','D',np.nan,'A','F'],
                 'Gender':[random.choice(['M','F']) for i in range (1,11)]})


#Filling all nan values of the dataframe

# filling marks column with mean

df['Marks']=np.where(df['Marks'].isnull(),df['Marks'].mean(),df['Grade'])
#filling grade column with mode
df['Grade']=np.where(df['Grade'].isnull(),df['Grade'].mode()[0],df['Grade'])

