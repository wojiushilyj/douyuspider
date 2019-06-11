import json
import urllib.request
import requests
import scrapy

url="http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=80"
res = scrapy.Request(url)
#res = urllib.request.urlopen(url)
data_list = json.loads(str(res))
#["data"]
#print(data_list)