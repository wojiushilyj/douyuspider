# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
import scrapy
from meinv.settings import IMAGES_STORE as images_store
from scrapy.pipelines.images import ImagesPipeline


class DouyuPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        """图片下载"""
        image_link = item["vertical_src"]
        # 2.管道将图片链接交给下载器下载
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        """图片重命名"""
        # 3.取出results中图片信息中：图片的存储路径
        # results是一个列表，列表中一个元组，元组中两个元素，第二个元素又是一个字典 / md5码
        # 推导式写法取值（最外层的列表相当于results列表）
        image_path = [x["path"] for ok, x in results if ok]

        # 4.为下载图片重命名
        # 4.os.rename(src_name, dst_name)
        #os.rename(self.images_store + "/"+img_path[0], self.images_store + "/" + item["message"] + ".jpg")
        os.rename(images_store + "/" + image_path[0], images_store + '/' + 'full/' + item['message'] + '.jpg')

        return item