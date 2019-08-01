# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class WanbiaomarketItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class WanbiaomarketItem(scrapy.Item):
    # 商品名称
    title = scrapy.Field()
    # 商品价格
    price = scrapy.Field()
    # 店铺名称
    store = scrapy.Field()
    # 商品编号（具有唯一性）
    pid = scrapy.Field()
    # 商品型号
    modelnumber = scrapy.Field()
    # 商品品牌
    brand = scrapy.Field()
    # 商品销量
    sales = scrapy.Field()
    # 商品参数
    desc = scrapy.Field()
    