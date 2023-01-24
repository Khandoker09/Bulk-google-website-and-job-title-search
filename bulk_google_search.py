'''
Date: 10.01.23
Author: Khandoker Tanjim Ahammad 
Purpose: Bulk google search form a csv or excel file for home page or linkedin page 
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
# for fixing the datafram with rows and columns 
################################################################################
df=pd.read_csv('test1.csv', index_col=False)
print(df.info())
df['company']=df['Unnamed: 0']
print(df.company)

df3 = df[df.index % 11 == 0]

df2=df[df['company'].str.contains("https")]
df2=df2[['company']]
df2.rename(columns={'company':'website'}, inplace=True)
print(df2.head(10))
#print(df3.head(20))
df4=pd.DataFrame(np.repeat(df3.company, 10))
print(df4.head(20))
print(df4.info())
# new_df = df4.merge(df2)
# print(new_df.head(20))
