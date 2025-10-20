import pandas as pd
import numpy as np
import random

#Data Frame

df=pd.DataFrame({'id':[i for i in range(1,11)],
                 'Marks':[23,24,24,np.nan,12,24,np.nan,34,24,57],
                 'Grade':['B','C','A',np.nan,'A','C','D',np.nan,'A','F'],
                 'Gender':[random.choice(['M','F']) for i in range (1,11)]})

#Ordinal Encoding on the Grade column along with filling nan values in the required column

#filling nan values in the grade column

df['Grade']=np.where(df['Grade'].isnull(),df['Grade'].mode()[0],df['Marks'])

#Encoding the grade column

df['Grade']=np.where(df['Grade']=='F',0,np.where(df['Grade']=='D',1,np.where(df['Grade']=='C',2,np.where(df['Grade']=='B',3,np.where(df['Grade']=='A',4,5)))))
print(df)