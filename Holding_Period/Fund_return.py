# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:55:53 2020

@author: HP
"""

import pandas as pd



#Change file path 
r_h = r'G:\Master_paper\Holding_Period\\'

#read NAV file
Fund_return = pd.read_excel(r_h+'Sample_NAV_Month.xlsx',sheet_name='Re_NAV')
Fund_return['Qx']=Fund_return.apply(lambda x: str(x['year'])+'Q'+str(int(x['month'])//3),axis =1)
Fund_list = list(Fund_return['Symbol'].unique())

#create two dataframe for return
Qx=[]
for years in range(2010,2019):
    for q in range(1,5):
        Qx.append(str(years)+'Q'+str(q))
    
Return_hy = pd.DataFrame(index=Fund_list,columns=Qx[1:])
Return_ay = pd.DataFrame(index=Fund_list,columns=Qx[3:])
#write return into dataframe
for i in Fund_return.index:
    if Fund_return['Qx'][i] in Qx[1:]:
        Return_hy.loc[Fund_return['Symbol'][i],Fund_return['Qx'][i]]=Fund_return['AccRt_hy'][i]
    if Fund_return['Qx'][i] in Qx[3:]:
        Return_ay.loc[Fund_return['Symbol'][i],Fund_return['Qx'][i]]=Fund_return['AccRt_ay'][i]
Return_ay.to_excel(r_h+'Return_ay.xlsx')
Return_hy.to_excel(r_h+'Return_hy.xlsx')