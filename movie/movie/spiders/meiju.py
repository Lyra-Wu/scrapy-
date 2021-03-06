# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector  
from movie.items import MovieItem
import sys

class MeijuSpider(scrapy.Spider):
    name = "meiju"
    allowed_domains = ["meijutt.com"]
    start_urls = ['http://www.meijutt.com/new100.html']
 
    #def parse(self, response):
       # movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        #for each_movie in movies:
            #item = MovieItem()
            #item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            #yield item
    def parse(self, response):  
            sel = Selector(response)  
            sites = sel.xpath('//ul[@class="top-list  fn-clear"]/li ')

            items = []

            for site in sites:  
                item = MovieItem()  
                item['title']  = site.xpath('./h5/a/@title').extract()
                #item['title'] = item['title'].encode("utf8")
                item['link'] = site.xpath('./h5/a/@href').extract()
                item['status'] = site.xpath('./span/font[@color="#AA3700"]/text()').extract()
                item['TV'] = site.xpath('./span[@class="mjtv"]/text()').extract()
                item['update_time'] = site.xpath('./div/font[@color="#AA3700"]/text()').extract() 
                item['class_'] = site.xpath('./span[@class="mjjq"]/text()').extract()
                items.append(item) 
            #print "crazylog:--(parse)-,type =",type(items),"value =",items
            #f = open("response.txt",'wb')
            #f.close()
            
            return items  

