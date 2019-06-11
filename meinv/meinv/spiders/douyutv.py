# -*- coding: utf-8 -*-
import scrapy
import json
from meinv.items import DouyuItem
import ssl



class DouyuSpider(scrapy.Spider):
    name = 'douyutv'
    allowed_domains = ['douyucdn.cn']
    ssl._create_default_https_context = ssl._create_unverified_context
    # 0.抓取斗鱼手机端app中颜值分类的数据包
    baseURL = "https://apiv2.douyucdn.cn/gv2api/rkc/roomlist/2_201/20/20/ios?client_sys=ios"
    offset = 20
    start_urls = ["https://apiv2.douyucdn.cn/gv2api/rkc/roomlist/2_201/%d/20/ios?client_sys=ios"%offset]
    #start_urls = ["https://apiv2.douyucdn.cn/gv2api/rkc/roomlist/2_201/20/20/ios?client_sys=ios"]

    def parse(self, response):
        # 1.将已经编码的json字符串解码为python对象(此处的Python对象时一个字典)
        # 1.data键对应的值是一个列表，列表中每一个元素又是一个字典
        #data_list = json.loads(response.body)["data"]
        json_string = json.loads(response.body)["data"]
        #json_string = json.dumps(jsonData1)
        #data_list = json.loads(json_string)["list"]
        data_list = json_string["list"]

        # 2.判断data是否为空（为空终止，不为空继续翻页）
        if not data_list:
            return

        for data in data_list:
            item = DouyuItem()
            #item["game_name"] = data["game_name"]
            item["room_id"] = data["room_id"]
            item["vertical_src"] = data["vertical_src"]
            item["nickname"] = data["nickname"]
            item["message"] =str(data ["room_id"]) + data["nickname"]
            #item["message"] = data["room_id"] + data["nickname"]

            # 3.返回item对象给管道进行处理
            yield item

        # 4.JSON文件只能通过翻页来爬取，不能通过xpath()提取
        self.offset += 20
        # 5.将请求发回给引擎，引擎返回给调度器，调度器将请求入队列
        #yield scrapy.Request(,callback=self.parse)
        yield scrapy.Request("https://apiv2.douyucdn.cn/gv2api/rkc/roomlist/2_201/40/20/ios?client_sys=ios" , callback=self.parse)
        #yield scrapy.Request("https://apiv2.douyucdn.cn/gv2api/rkc/roomlist/2_201/20/20/ios?client_sys=ios",callback=self.parse)