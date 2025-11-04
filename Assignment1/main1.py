import pandas as pd
import numpy as np
import random
try:
  def ordinalencoding(df,col,ranklist):
    indexlist=[i for i in range(0,len(ranklist))]
    zippedlist=list(zip(ranklist,indexlist))
    for i in zippedlist:
      np.where(df[col]==i[0],i[1],df[col])
    return df
  
  if __name__="__main__":
    df=pd.DataFrame({'id':[i for i in range(1,11)],
                     'Marks':[23,24,24,np.nan,12,24,np.nan,34,24,57],
                     'Grade':['B','C','A',np.nan,'A','C','D',np.nan,'A','F'],
                     'Gender':[random.choice(['M','F']) for i in range (1,11)]})
    
    print(ordinalencoding(df,'Grade',['A','B','C','D','E','F']))
except Exception as e:
  print(e)
