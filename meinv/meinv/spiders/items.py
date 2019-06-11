# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # 1.主播所在版块
    game_name = scrapy.Field()

    # 2.主播房间号
    room_id = scrapy.Field()

    # 3.主播链接
    vertical_src = scrapy.Field()

    # 4.主播昵称
    nickname = scrapy.Field()

    # 存储照片名称信息5.
    message = scrapy.Field()
