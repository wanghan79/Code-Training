import phylopandas as ph
import string
import pandas as pd
df1 = ph.read_fasta('uniprot-membrane .fasta')
df2=ph.read_fasta('Uniq_MP.fasta')
#print(df1.columns.values.tolist())   # 列名称
#print(df1.shape[0])
#print(df2.columns.values.tolist())   # 列名称
#print(df2.shape[0])
count=1
f = open('01_2000pro.fasta', 'w')
for i in range(0,len(df1)):
     for j in range(0,len(df2)):
        str=df1.loc[i]['id'].split('|')[1]
        if( str==df2.loc[j]['id'] ):
            break
     else :
            f.write('>' + str+ '\n')
            f.write(df1.loc[i]['sequence'] + '\n')
            count=count+1
         #如果对比不同，则写入文档
     if(count>2000) :
         break
