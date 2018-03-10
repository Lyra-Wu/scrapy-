# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class MoviePipeline(object):
 #   def process_item(self, item, spider):
  #      return item
  #class MoviePipeline(object):
    #def process_item(self, item, spider):
        #with open("my_meiju.txt",'a') as fp:
            #fp.write(item['name'].encode("utf8") + '\n')
class MoviePipeline(object):
    def process_item(self, item_jsgh, spider):
        # with open("my_meiju.txt",'a') as fp:
        #     fp.write(item['title'].encode("utf8") + '\n')
        #     fp.write(item['link'].encode("utf8") + '\n')
        #     fp.write(item['class'].encode("utf8") + '\n')
        # for item in item_jsgh:
        #     print "-------------sgh -",item

        # print "crazylog:--(process_item)-,type =",type(item_jsgh),"value =",item_jsgh
        pass
            