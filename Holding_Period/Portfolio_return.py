# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:36:44 2020

@author: HP
"""

import pandas as pd
import datetime

starttime = datetime.datetime.now()
#Change file path 
r_h = r'G:\Master_paper\Holding_Period\\'

names=locals()

#read portfolio file from 1-9
for i in range(1,10):
    names['Portfolio'+str(i)]=pd.read_csv(r_h+'Portfolio'+str(i)+'_weight.csv',index_col = 0)
    names['Portfolio'+str(i)+'_weight'] = pd.DataFrame(index = names['Portfolio'+str(i)].index)
    for col in names['Portfolio'+str(i)].columns[1:]:
        if int(col[:4]) >2009 and int(col[-2:])%3 ==0:
            names['Portfolio'+str(i)+'_weight'][col[:4]+'Q'+str(int(col[-2:])//3)] = names['Portfolio'+str(i)][col]

print('Succeed in loading protfolio weight data!\n' )

#reset columns of return_hy and return_ay
column_1 = Portfolio1_weight.columns[:-1]
column_2 = Portfolio1_weight.columns[:-3]

#read fund return file
Return_hy=pd.read_excel(r_h+'Return_hy.xlsx',header = None, skiprows = [0],index_col = 0,names=column_1)
Return_ay=pd.read_excel(r_h+'Return_ay.xlsx',header = None, skiprows = [0],index_col = 0,names=column_2)
print('Succeed in loading protfolio return data!\n' )

for freq in ('hy','ay'):
    for p in range(1,10):
        names['Rt_fund_'+str(p)+'_'+freq]=pd.DataFrame(index=names['Return_'+freq].index,columns=names['Return_'+freq].columns)
        
        for i in names['Rt_fund_'+str(p)+'_'+freq].index:
            for j in names['Rt_fund_'+str(p)+'_'+freq].columns:    
                names['Rt_fund_'+str(p)+'_'+freq].loc[i,j] = names['Return_'+freq].loc[i,j]*names['Portfolio'+str(p)+'_weight'].loc[i,j]
                print(freq,p,i,j)
        names['Rt_ptf_'+str(p)+'_'+freq]=pd.DataFrame(names['Rt_fund_'+str(p)+'_'+freq].sum(axis=0),columns=['Rt'])
        names['Rt_ptf_'+str(p)+'_'+freq].to_excel(r_h+'Rt_ptf_'+str(p)+'_'+freq+'.xlsx')
        
#compute the duration time        
endtime = datetime.datetime.now()
deltatime = endtime - starttime
print('Program completed in %d minutes and %.2f seconds!'%(deltatime.seconds//60,deltatime.seconds%60))
