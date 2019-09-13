import phylopandas as ph
import string
from Bio import SeqIO
import pandas as pd
import numpy as np
df1=ph.read_fasta('1568122732.fas.db2novel')
f = open('Negative_Samples.fasta', 'w')
print(df1.shape[0])
#list=random.sample([i for i in range(len(df1))],10)
list=np.random.choice(range(len(df1)),271, replace=False)#随机选取271序号
#print(list)
for i in range(len(list)):
    f.write('>' + df1.loc[list[i]]['id'] + '\n')
    f.write(df1.loc[list[i]]['sequence'] + '\n')
