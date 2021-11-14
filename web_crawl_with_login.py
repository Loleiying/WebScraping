# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:27:24 2020

@author: Liying Lu
"""

#%%
## login to Blueprint
#import requests
#
#post_login_url = ""
#username = ""
#password = ""
#
#request_url = ""
#
## login information
#payload = {
#		"_username" : username,
#		"_password" : password
#		}
#
#with requests.Session() as session:
#	post = session.post(post_login_url, data = payload)
#	r = session.get(request_url)
#	#print(r.text)

#%%
#from lxml import html
#webpage = html.fromstring(r.text)
#webpage.xpath('//a/@href')

#from bs4 import BeautifulSoup as bs
#soup = bs(r.text, 'html.parser')
#table = soup.find(lambda tag: tag.name=="table" 
#				  and tag.has_attr('id')
#				  and tag['id'] == "campaign_grid_view")
#rows = table.findAll(lambda tag: tag.name=='tr')
#print(rows)

## check if the request url returns as the actual html
## PROBLEM: the session cannot get the request_url, it turns out it is stuck at the login page/
## WHY
#campaign_html = open('C:\\Users\\liyin\\Documents\\GitHub\\DataReport\\campaigns_html.txt', 'w+')
#campaign_html.write(r.text)
#campaign_html.close()
