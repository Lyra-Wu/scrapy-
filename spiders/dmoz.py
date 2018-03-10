# -*- coding: utf-8 -*-
import scrapy


class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = ['http://dmoz.org/']

    def parse(self, response):
        #pass
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)