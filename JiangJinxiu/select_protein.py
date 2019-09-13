# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 12:40:27 2019

@author: hp
"""
import phylopandas as ph
import string
from Bio import SeqIO
import pandas as pd
class Seclect:
    def select_protein(self,df1):
        #print(df1._stat_axis.values.tolist()) # 行名称
        #print(df1.columns.values.tolist())# 列名称
        data1=df1[['id','sequence']]
        count=0
        data=data1.astype(str)
        y=data[data['sequence'].str.contains('J|O|U|X|Z|B')]
        #print(y['sequence'])   #要删除的蛋白序列
        k=y._stat_axis.values.tolist()  #要删除的蛋白序列编号
        #print(k)
        for i in range(0, len(data)):
            for index in range(0,len(k)):
                if k[index]==i:
                 count=count+1
                 data.drop([i], inplace=True)
        data=data.reset_index(drop = True)#！！！一定重构，不重构肯定报错
        for i in range(0, len(data)):
            if(len(data.loc[i]['sequence'])<50):
                 #print(i)
                 count=count+1
                 #print(count)  #删除的个数
                 data.drop([i], inplace=True)
        data = data.reset_index(drop=True)
        return data
'''if __name__ == '__main__':
    df1 = ph.read_fasta('01_2000pro.fasta')
    data=Seclect().select_protein(df1)
    print(data.shape[0]) #最后剩余的蛋白序列的个数
    f = open('new_01_2000pro.fasta', 'w')
    for i in range(0,len(data)):
        f.write('>'+data.loc[i]['id']+'\n')
        f.write(data.loc[i]['sequence'] + '\n')
'''



