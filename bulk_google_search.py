'''
Date: 09.01.23
Author: Khandoker Tanjim Ahammad
Purpose: search a term in google and save it in a excel file 
parameter="stop"  is the para resposible for the number of search link added to output
'''
import pandas as pd
from googlesearch import search
from random import randint
import time
##################################################################################
input_df=pd.read_excel('/content/test_file.xlsx',index_col=False)
input_df = input_df.reset_index()
list=input_df['companyname'].to_list()
print(list)
###################################################################################

df_raw = pd.DataFrame(columns=['companyname','probable_website'])
#query = "Christian Preussh Axel Spriger"
#list=['20 Minuten', '20 Minutes', '24 heures & Tribune de GenÃƒÆ’Ã‚Â¨ve', '84XO']
for query in list:
    df_raw.loc[query, ['companyname']] = randint(0,99)
    for i in search(query, tld="co.in", num=10, stop=10, pause=2):
        df_raw.loc[i, ['probable_website']] = randint(0,99)

print (df_raw.info()) 
print(df_raw.head)


#df=pd.read_excel('test1.xlsx', index_col=False)
df=df_raw
print(df.info())
df['company']=df['Unnamed: 0']
# print(df.info())
# print(df.head())
###################################################################
## extracting the only the right column
###################################################################
df2=df[['company']]
#print(df2.head(20))
###################################################################
## extracting website from the data columns 
###################################################################
df_web=df2[df2['company'].str.contains("https")]
df_web=df_web[['company']]
df_web.rename(columns={'company':'probable_website'}, inplace=True)
#df_web["count"] = df_web.apply(lambda _: 10, axis=1)
print(df_web.head(10))
###################################################################
## extracting the company name from the data 
###################################################################
df_com = df2[df2.index % 11 == 0]
df_com=df_com['company']
df_com = df_com.reset_index()
#print(df_com.head(20))
##################################################################
## merge company name and website for
##################################################################
df_com["count"] = df_com.apply(lambda _: 12, axis=1)
df_com = df_com.loc[df_com.index.repeat(df_com['count'])].reset_index(drop=True)
df_com=df_com[['company']]
#print(df_com.head(20))
####################################################################
##  merging and making the final datasets 
####################################################################
df_final=pd.DataFrame(pd.concat([df_com,df_web],keys = ['company','probable_website'],axis=1))

print(df_final.head(20))
df_final.to_excel('final_file.xlsx')


from google.colab import files
files.download('/content/final_file.xlsx')

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
