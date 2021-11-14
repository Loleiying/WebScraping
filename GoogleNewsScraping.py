# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 12:37:56 2021

@author: Liying Lu

This code allows you to scrape news title or news website from GoogleNews.
"""
#%% import libraries
from GoogleNews import GoogleNews # pip install GoogleNews
from newspaper import Article # pip install newspaper
from newspaper import Config
import pandas as pd
import nltk
import xlsxwriter

#config will allow us to access the specified url for which we are 
#not authorized. Sometimes we may get 403 client error while parsing 
#the link to download the article.
# nltk.download('punkt')

#%% scrape news from api
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

# CHANGE INPUTS HERE
start_date = '01/01/2020'
end_date = '12/8/2020'
search_term = ''

# retrieve data from API
googlenews=GoogleNews(start=start_date ,end=end_date)
googlenews.search(search_term)
result=googlenews.result()

#%% data cleaning
# obtain only the media / news organization
media = []
df=pd.DataFrame(result)
media.append(df.media.unique().tolist())

# parse data
for i in range(1,20):
    googlenews.getpage(i)
    result=googlenews.result()
    df=pd.DataFrame(result)
    media.append(df.media.unique().tolist())

# store all media in one list
result = []
for ls in media:
    result.extend(ls)
print(len(result))

# remove duplicates
output = set(result)
A = []
for i in output:
    if i!= "":
        A.append(i)
print(len(A))


#%% Write cleaned data to spreadsheet
with xlsxwriter.Workbook('test.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    row = 0
    column = 0

    # iterating through content list 
    for item in A : 
        # write operation perform 
        worksheet.write(row, column, item) 
        row += 1
    workbook.close() 





