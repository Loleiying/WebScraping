# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:21:16 2021

@author: ll8922
"""

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quote"
    start_urls = [
        'https://bluelimelearning.github.io/my-fav-quotes/'
        ]
    
    def parse(self, response):
        # HTTP request will send a response object back
        for quote in response.css('div.quotes'):
            yield {
                'quote':quote.css('p.aquote::text').extract(),
                'author':quote.css('p.author::text').extract_first()
                }