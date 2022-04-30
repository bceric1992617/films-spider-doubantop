# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql 
import scrapy
import os
import shutil
import time
import datetime
from scrapy.pipelines.images import ImagesPipeline
from doubantop.settings import IMAGES_STORE
from doubantop.getFilmMsg import getFilmMsg


class doubantopPipeline: 
    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            port=3306, 
            db='films', 
            user='root', 
            passwd='123321', 
            charset='utf8'
        )
        self.db_cur = self.db.cursor()

    def process_item(self, item, spider):
        #更新和插入信息
        self.updateMsg(item)
        self.db.commit() 
        return item

    def updateMsg(self, item):
        for i in range(len(item['name'])):
            insertSql = 'insert into doubanTop(filmsId,filmsName,createTime,updateTime,isDel) values(%s,%s,%s,%s,%s)'
            updateSql ='update films set douban=%s where filmsId=%s'
            title = item['name'][i].replace(' ','')
            self.db_cur.execute("select filmsId from films where filmsName= '"+ title +"' limit 1;")
            filmMsg = self.db_cur.fetchone()
            if bool(filmMsg) :
                self.db_cur.execute(updateSql, [
                    item['douban'][i],
                    filmMsg
                ])

                self.db_cur.execute(insertSql, [
                    filmMsg,
                    title,
                    int(round(time.time())),
                    int(round(time.time())),
                    0            
                ])
            
            




        

