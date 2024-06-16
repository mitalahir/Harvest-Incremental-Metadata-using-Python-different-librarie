import pandas as pd
import numpy as np

df1 = pd.DataFrame()
df2 = pd.read_csv("Handleid.csv")
df2.head()
                                                                 
df2.set_index('handleid')
df2.head()
                                                               
#read all csv metadata files and find the number of zeros(%) 
       for index, row in df2.iterrows():
            no = row['handleid'] #.astype(str)
            df = pd.read_csv("xyz.csv")
            df3 = df[df['dc.identifier.uri'].str.contains(no, na=False)]
            df1 = df1.append(df3)
    #df1 = df1.append({'HandleId': no, 'dcidentifieruri': df3}, ignore_index=True)

df1

df1.to_csv("Output_xyz_Univesity.csv", index=False)
