# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.http import Request
# import the Structured data mudule from item
from pic.items import PicItem

class XhSpider(scrapy.Spider):
    # Crawler name, unique
    name = "xh"
    # domain allowed to be accessed
    allowed_domains = ["xiaohuar.com"]
    # the initial URL
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']
   
    # Set an empty collection
    url_set = set()
    def parse(self, response):
        # if the image address start with http://www.xiaohuar.com/list-，I will get it's name and address
        if response.url.startswith("http://www.xiaohuar.com/list-"):
            allPics = response.xpath('//div[@class="img"]/a')
            for pic in allPics:
                # Process each image separately, take out its' name and address.
                item = PicItem()
                name = pic.xpath('./img/@alt').extract()[0]
                addr = pic.xpath('./img/@src').extract()[0]
                addr = 'http://www.xiaohuar.com'+addr
                item['name'] = name
                item['addr'] = addr
                # Return crawled data
                yield item
        # get all the address links 
        urls = response.xpath("//a/@href").extract()
        for url in urls:
            # if address start with http://www.xiaohuar.com/list-，and not in the collection, get the message
            if url.startswith("http://www.xiaohuar.com/list-"):
                if url in XhSpider.url_set:
                    pass
                else:
                    XhSpider.url_set.add(url)
                    # the default callback function is parse, you can assign it 
                    # by 'from scrapy.http import Request'
                    # from scrapy.http import Request
                    # Request(url,callback=self.parse)
                    yield self.make_requests_from_url(url)
            else:
                pass
    
 

