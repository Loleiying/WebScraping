# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:01:37 2021

@author: ll8922
"""

# import libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# get url
quotes_page = 'https://bluelimelearning.github.io/my-fav-quotes/'

# open connection to get client.HTTPResponse
uClient = uReq(quotes_page)
# read webpage to bytes
page_html = uClient.read()
# close connection
uClient.close()
# parse html
page_soup = soup(page_html, "html.parser")


# extract data from formatted html
quotes = page_soup.findAll("div", {"class":"quotes"})

for quote in quotes:
    # get the quote
    fav_quote = quote.findAll("p", {"class":"aquote"})
    aquote = fav_quote[0].text.strip()
    
    # get the author
    fav_authors = quote.findAll("p", {"class":"author"})
    author = fav_authors[0].text.strip()
    
    print(author)
    print(aquote)