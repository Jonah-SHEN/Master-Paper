# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 00:18:22 2020

@author: HP
"""

import pandas as pd

#Change file path 
r_h = r'G:\Master_paper\Holding_Period\\'

names=locals()

#read free risk rate data
Rf =pd.read_excel(r_h+'Free_risk_rate.xlsx',index_col = 0)
Rm =pd.read_excel(r_h+'Market_return.xlsx',skiprows=[1,2,3,4],header = 0)
delay = {'hy':1,'ay':3}
for freq in ('hy','ay'):
    #read three factor data
    names['Factor_3_'+freq] = pd.read_excel(r_h+'Factor_3_'+freq+'.xlsx')
    #create concrete dataframe containing all return 
    names['Rt_ptf_all_'+freq]=pd.DataFrame(index =names['Factor_3_'+freq].index)
    names['Rt_ptf_all_'+freq]['RMRF'] = list(names['Factor_3_'+freq]['RMRF_'+freq])
    names['Rt_ptf_all_'+freq]['SMB'] = list(names['Factor_3_'+freq]['SMB_'+freq])
    names['Rt_ptf_all_'+freq]['HML'] = list(names['Factor_3_'+freq]['HML_'+freq])
    names['Rt_ptf_all_'+freq]['Rm'] = list(Rm['Rm_'+freq][delay[freq]:])
    #read portfolio return data
    for p in range(1,10):
        names['Rt_ptf_'+str(p)+'_'+freq]=pd.read_excel(r_h+'Rt_ptf_'+str(p)+'_'+freq+'.xlsx',index_col = 0)
        names['Rt_ptf_'+str(p)+'_'+freq]['Rf'] = list(Rf['Rf_'+freq][delay[freq]:])
        names['Rt_ptf_'+str(p)+'_'+freq]['Rm'] = list(Rm['Rm_'+freq][delay[freq]:])
        names['Rt_ptf_all_'+freq]['Rt_f'+str(p)] = list(names['Rt_ptf_'+str(p)+'_'+freq]['Rt'] - names['Rt_ptf_'+str(p)+'_'+freq]['Rf'])
        names['Rt_ptf_all_'+freq]['Rt_m'+str(p)] = list(names['Rt_ptf_'+str(p)+'_'+freq]['Rt'] - names['Rt_ptf_'+str(p)+'_'+freq]['Rm'])
        names['Rt_ptf_all_'+freq]['Rt'+str(p)] = list(names['Rt_ptf_'+str(p)+'_'+freq]['Rt'])
#        names['Rt_ptf_'+str(p)+'_'+freq]['Rt_f'] =names['Rt_ptf_'+str(p)+'_'+freq]['Rt'] - names['Rt_ptf_'+str(p)+'_'+freq]['Rf']
#        names['Rt_ptf_'+str(p)+'_'+freq]['RMRF'] = list(names['Factor_3_'+freq]['RMRF_'+freq])
#        names['Rt_ptf_'+str(p)+'_'+freq]['SMB'] = list(names['Factor_3_'+freq]['SMB_'+freq])
#        names['Rt_ptf_'+str(p)+'_'+freq]['HML'] = list(names['Factor_3_'+freq]['HML_'+freq])
#        names['Rt_ptf_'+str(p)+'_'+freq].to_excel(r_h+'Rt0_ptf_'+str(p)+'_'+freq+'.xlsx')
        names['Rt_ptf_all_'+freq].to_excel(r_h+'Rt_ptf_all_'+freq+'.xlsx')