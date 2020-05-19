# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:18:59 2020

@author: HP
"""

import pandas as pd
import numpy as np
import sys


#Change file path 
r_h = r'G:\Master_paper\Holding_Period\\'

#PROCESSING********************************************************************
#read data file of book value, size and market cap
Book_value = pd.read_excel(r_h+'Processed_data.xlsx',sheet_name='book_equity')
Size = pd.read_excel(r_h+'Processed_data.xlsx',sheet_name='Size_4')
Market_value = pd.read_excel(r_h+'Processed_data.xlsx',sheet_name='Mkt_cap2')

#test if the lengths of three dataframe are same
if len(Book_value.index) == len(Market_value.index) and len(Book_value.index) == len(Size.index):
    print('Successed in reading data!\n')
else:
    print('Warning:Data reading structure problem!\n')
  
#Process the three dataframes with the following standards:
#the datasets are downloaded from Wind on 20th,March 2020, containing stocks liseted after 2017
#if the list date(index) is late than 2017, delete the row
#if value is nagetive, then set the value to NAN
#if the year of the value(columns) is no late than the list date,then set the value to NAN
#the change in one dataframe should apply to the other two simutaneouly 
# process step 1:
Book_value=Book_value.drop(Book_value[Book_value['year']>2017].index)
Size=Size.drop(Size[Size['year']>2017].index)
Market_value=Market_value.drop(Market_value[Market_value['year']>2017].index)

# process step 2 & 3:
for j in Book_value.columns[4:]:    
    for i in Book_value.index:
        if int(Book_value['year'][i])>int(j) or Book_value.loc[i,j] <= 0 or Size.loc[i,j] <=0 or Market_value.loc[i,j] <=0: 
            Book_value.loc[i,j] = np.nan
            Size.loc[i,j] = np.nan
            Market_value.loc[i,j] = np.nan
#test if the index and columns are the same 
index_true = (Book_value['code']==Market_value['code']).all() and (Book_value['code']==Size['code']).all()
col_true = (Book_value.columns==Market_value.columns).all() and (Book_value.columns==Size.columns).all()
if index_true and col_true:
    print('Successed in processing data!\n')
else:
    sys.exit('fail in processing data!\n')
    
#calculate BM : Book value over market value:
BM = pd.DataFrame(index = Book_value.index,columns = Book_value.columns)
BM.loc[:,:4] = Book_value.iloc[:,:4]
for j in BM.columns[4:]:
    BM.loc[:,j] = Book_value.loc[:,j]/Market_value.loc[:,j]
BM.to_excel(r_h+'BM.xlsx')

#GROUPING********************************************************************
#define new dataframe for six group
#Group 1 to 6 means SL\SM\SH\BL\BM\BH
Group = pd.DataFrame()
Group['code'] =Size['code']
for i in range(2009,2019):
    years=i-1
    Size[str(years)+'_SMB'] = Size[years].map(lambda x: 3 if x >= Size[years].median() else np.nan)
    Size[str(years)+'_SMB'] = Size.apply(lambda row: 0 if row[years] < Size[years].median() else row[str(years)+'_SMB'],axis=1)
    border_down, border_up = BM[years].quantile([0.3, 0.7])
    BM[str(years)+'_HML'] = BM[years].map(lambda x: 3 if x >= border_up  else np.nan)
    BM[str(years)+'_HML'] = BM.apply(lambda row: 1 if row[years] < border_down else row[str(years)+'_HML'], axis=1)
    BM[str(years)+'_HML'] = BM.apply(lambda row: 2 if (row[years] >= border_down) and(row[years] < border_up) else row[str(years)+'_HML'], axis=1)
    
    Group[i]=BM[str(years)+'_HML']+Size[str(years)+'_SMB']
Group.reset_index(drop=True,inplace=True)
Group.to_excel(r_h+'Group.xlsx')

        