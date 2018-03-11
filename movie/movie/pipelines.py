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
    def process_item(self, item, spider):
        with open("my_meiju.txt",'a') as fp:
         #for item in item_jsgh:http://www.meijutt.com/content/meiju23093.html
        # for item in item_jsgh:
            # if len(item['title']) >= 1:
            #     if len(item['link']) >=1:
            #         if len(item['class_']) >=1:
            #             if len(item['status']) >=1:
            #                 if len(item['TV']) >=1:
            #                     if len(item['update_time']) >=1:
            #                         fp.write("剧名: " + item['title'][0].encode("utf8") + '\n')
            #                         fp.write("链接: " + "http://www.meijutt.com" + item['link'][0].encode("utf8") + '\n')
            #                         fp.write("类型: " + item['class_'][0].encode("utf8") + '\n')
            #                         fp.write("更新状态: " + item['status'][0].encode("utf8") + '\n')
            #                         fp.write("电视台: " + item['TV'][0].encode("utf8") + '\n')
            #                         fp.write("更新时间: " + item['update_time'][0].encode("utf8") + '\n' + '\n')

            cnt =0
            for key in item:
                if len(item[key]) >0:
                    cnt = cnt +1
            
            if cnt == len(item):
                fp.write("剧名: " + item['title'][0].encode("utf8") + '\n')
                fp.write("链接: " + "http://www.meijutt.com" + item['link'][0].encode("utf8") + '\n')
                fp.write("类型: " + item['class_'][0].encode("utf8") + '\n')
                fp.write("更新状态: " + item['status'][0].encode("utf8") + '\n')
                fp.write("电视台: " + item['TV'][0].encode("utf8") + '\n')
                fp.write("更新时间: " + item['update_time'][0].encode("utf8") + '\n' + '\n')
                
                    
                


        # for item in item_jsgh:
        #     print "-------------sgh -",item

            #print "crazylog:--(process_item)-,type =",type(item['title']),"value =",item['title']
        
            