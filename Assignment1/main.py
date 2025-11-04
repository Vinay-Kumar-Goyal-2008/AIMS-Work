import pandas as pd
import numpy as np
import random
try:
  def onehotencoder(df,col):
    uniqueelements=df[col].unique()
    for i in uniqueelements:
      df[i]=np.where(df[col]==i,1,0)
    df=df.drop(columns=[col])
    return df
  
  
  if __name__=="__name__":
    
    df=pd.DataFrame({'id':[i for i in range(1,11)],
                     'Marks':[23,24,24,np.nan,12,24,np.nan,34,24,57],
                     'Grade':['B','C','A',np.nan,'A','C','D',np.nan,'A','F'],
                     'Gender':[random.choice(['M','F']) for i in range (1,11)]})
    print(onehotencoder(df,'Gender'))
except Exception as e:
  print(e)
