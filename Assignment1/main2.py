import pandas as pd
import numpy as np
import random

#Data Frame

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
try:
    ch=int(input('Enter the choice:- '))
except Exception as e:
    print(e)
if (ch==1):
    df['Marks']=np.where(df['Marks'].isnull(),df['Marks'].mode()[0],df['Grade'])
elif (ch==2):
    df['Marks']=np.where(df['Marks'].isnull(),df['Marks'].median(),df['Grade'])
elif ch==3:
    df['Marks']=np.where(df['Marks'].isnull(),df['Marks'].mean(),df['Grade'])
elif ch==4:
    df=df.dropna(subset=['Marks'])
else:
    print("Wrong choice!")
#filling grade column with mode
df['Grade']=np.where(df['Grade'].isnull(),df['Grade'].mode()[0],df['Grade'])
print('filled the nan values in the grade column with mode')
