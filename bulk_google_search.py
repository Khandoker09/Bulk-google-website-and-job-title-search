'''
Date: 10.01.23
Author: Khandoker Tanjim Ahammad 
Purpose: Bulk google search form a csv 
'''
import pandas as pd
from googlesearch import search
from random import randint
import time
################################################################################
input_df=pd.read_excel('/content/Akita List January 2023.xlsx',index_col=False)
input_df = input_df.reset_index()
list=input_df['Name'].to_list()
print(list)
################################################################################

df = pd.DataFrame(columns=['companyname','probable_website'])
#query = "Christian Preussh Axel Spriger"
#list=['20 Minuten', '20 Minutes', '24 heures & Tribune de GenÃƒÆ’Ã‚Â¨ve', '84XO']
for query in list:
    df.loc[query, ['companyname']] = randint(0,99)
    for i in search(query, tld="co.in", num=10, stop=1, pause=2):
        df.loc[i, ['probable_website']] = randint(0,99)

print (df.info()) 
print(df.head)
df.to_csv('test1.csv')
################################################################################
