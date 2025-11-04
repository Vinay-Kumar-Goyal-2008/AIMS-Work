import pandas as pd
import numpy as np
import random

def imputer(df,col,how):
  stratlist=['mean','median','mode','drop']
  if ((how-1)<0):
    return 'Wrong input'
  how=stratlist[how-1]
  try:
    if (how=='mean'):
      df[col]=df[col].fillna(df[col].mean())
    elif (how=='mode'):
      df[col]=df[col].fillna(df[col].mode()[0])
    elif (how=='median'):
      df[col]=df[col].fillna(df[col].median())
    elif (how=='drop'):
      df.dropna(subset=[col])
    else:
      return "Wrong input"
    return df
  except Exception as e:
    return e
try:
  if __name__=='__main__':
    df=pd.DataFrame({'id':[i for i in range(1,11)],
                     'Marks':[23,24,24,np.nan,12,24,np.nan,34,24,57],
                     'Grade':['B','C','A',np.nan,'A','C','D',np.nan,'A','F'],
                     'Gender':[random.choice(['M','F']) for i in range (1,11)]})
    
    
    #Filling all nan values of the dataframe
    print('How do you want to fill the null values in the marks column')
    print('''1. Mode
          2. Median
          3.Mean
          4. Drop the rows''')
        ch=int(input('Enter the choice:- '))
    print(imputer(df,'Marks',3))
except Exception as e:
  print(e)
