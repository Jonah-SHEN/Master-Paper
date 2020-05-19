# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:18:09 2020

@author: HP
"""

import pandas as pd
import datetime
import sys

def cal_factor(t,Rt,Gt):
    if len(Rt) != len(Gt):
        sys.exit('Warning!'+str(t)+'Go Wrong!')
    temp_df=pd.DataFrame()
    temp_df['Rt'],temp_df['Gt']=Rt,Gt
    
    smb=(temp_df[(temp_df['Gt']==1)]['Rt'].mean()+temp_df[(temp_df['Gt']==2)]['Rt'].mean()+temp_df[(temp_df['Gt']==3)]['Rt'].mean())/3\
    -(temp_df[(temp_df['Gt']==4)]['Rt'].mean()+temp_df[(temp_df['Gt']==5)]['Rt'].mean()+temp_df[(temp_df['Gt']==6)]['Rt'].mean())/3

    hml=(temp_df[(temp_df['Gt']==3)]['Rt'].mean()+temp_df[(temp_df['Gt']==6)]['Rt'].mean())/2-(temp_df[(temp_df['Gt']==1)]['Rt'].mean()+temp_df[(temp_df['Gt']==4)]['Rt'].mean())/2
    
    return smb,hml

time0=datetime.datetime.now()
#Change file path 
r_h = r'G:\Master_paper\Holding_Period\\'

names=locals()
Rt_hy = pd.read_excel(r_h+'Return.xlsx',sheet_name='rolling_half_year_return')
Rt_ay = pd.read_excel(r_h+'Return.xlsx',sheet_name='rolling_year_return')
Group = pd.read_excel(r_h+'Group.xlsx')
Rm = pd.read_excel(r_h+'Market_return.xlsx',skiprows=[1,2,3,4])

#signal for same code test
if (Rt_ay['code']==Group['code']).all() and (Rt_hy['code']==Group['code']).all():
    print('Successed in reading data!\n')
else:
    sys.exit('fail in reading data!\n')
    
#calculate different factors in two frequency
delay ={'ay':3,'hy':1}
for freq in ['ay','hy']:
#define SMB_hy,HML_hy, SMB_ay,HML_ay  four dataframe with index equal to time series
    names['SMB_'+freq]=pd.DataFrame(index=names['Rt_'+freq].columns[1:],columns=['SMB'])
    names['HML_'+freq]=pd.DataFrame(index=names['Rt_'+freq].columns[1:],columns=['HML'])
#calculate each SMB HML factor to above dataframe
    for i in names['Rt_'+freq].columns[1:]:
        year,window=i.split('Q')[0],i.split('Q')[1]
#        print(year,window)
        if window == '1_2' or window =='1_4':
            result= cal_factor(i,names['Rt_'+freq][i],Group[int(year)-1])
        else:
            result= cal_factor(i,names['Rt_'+freq][i],Group[int(year)])
        names['SMB_'+freq].loc[i,'SMB'],names['HML_'+freq].loc[i,'HML'] = result[0],result[1] 

#define three factors dataframe
    if len(names['Factor_3_'+freq].index) == len(Rm['RMRF_'+freq][delay[freq]:].index):
        print('Succeeded in constructing three factors!\n')
    else:
        sys.exit('fail in constructing three factors!\n')
    names['Factor_3_'+freq] = pd.DataFrame(index=names['Rt_'+freq].columns[1:])
    names['Factor_3_'+freq]['RMRF_'+freq] = list(Rm['RMRF_'+freq][delay[freq]:])
    names['Factor_3_'+freq]['SMB_'+freq] = names['SMB_'+freq]['SMB']
    names['Factor_3_'+freq]['HML_'+freq] = names['HML_'+freq]['HML']
    names['Factor_3_'+freq].to_excel(r_h+'Factor_3_'+freq+'.xlsx')
    
time1= datetime.datetime.now()
delta_time = time1-time0
print('Congratulations! Calculation took %f seconds\n'%delta_time.seconds)  
