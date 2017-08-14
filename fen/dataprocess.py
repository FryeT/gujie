
import pandas as pd
import os

dirpath = 'datas'

files = os.listdir(dirpath)
files.sort(key=lambda x: int(os.path.splitext(x)[0]))
dfcols = ['s_200','s_400','m_200','m_400','s_c','m_c']
df = pd.DataFrame(columns=dfcols)
for file in files:
    temp_df = pd.read_table(os.sep.join((dirpath,file)))
    temp_df.columns = dfcols
    df = pd.concat([df,temp_df],ignore_index=True)

df.to_csv('processed_data.csv',index=False)
