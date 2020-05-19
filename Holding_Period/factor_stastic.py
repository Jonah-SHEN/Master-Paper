# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:12:09 2020

@author: HP
"""

import pandas as pd
from scipy import stats
r_h = r'G:\Master_paper\Holding_Period\\'

names=locals()
Statis = ['mean','PTP','std','CV','min','25%','50%','75%','max','skew','kurt']

Factor_3_ay = pd.read_excel(r_h+'Factor_3_ay.xlsx',index_col=0)
Factor_3_hy = pd.read_excel(r_h+'Factor_3_hy.xlsx',index_col=0)

Fct_3_stat=pd.DataFrame(index=Statis,columns=list(Factor_3_ay.columns)+list(Factor_3_hy.columns))

for freq in ['ay','hy']:
    for column in names['Factor_3_'+freq].columns:
        for item in range(len(names['Factor_3_'+freq][column].describe().index)):
            Fct_3_stat.loc[names['Factor_3_'+freq][column].describe().index[item],column]= names['Factor_3_'+freq][column].describe()[item]
        Fct_3_stat.loc['PTP',column] =  Fct_3_stat.loc['max',column]- Fct_3_stat.loc['min',column]
        Fct_3_stat.loc['CV',column] =  Fct_3_stat.loc['mean',column]/Fct_3_stat.loc['std',column]
        Fct_3_stat.loc['skew',column] = stats.skew(names['Factor_3_'+freq][column])
        Fct_3_stat.loc['kurt',column] = stats.kurtosis(names['Factor_3_'+freq][column])

Fct_3_stat.to_excel(r_h+'Fct_3_stat.xlsx')
