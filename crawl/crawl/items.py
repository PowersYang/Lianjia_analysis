# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class House(scrapy.Item):
    className = 'house'
    
    # 房屋基本信息
    houseTitle = scrapy.Field() # 房屋标题
    houseTotalMoney = scrapy.Field() #房屋总价
    houseSinglePrice = scrapy.Field() # 房屋单价
    houseDownPayment = scrapy.Field() # 房屋首付
    houseGardenName = scrapy.Field() # 小区名称
    houseLocation = scrapy.Field() # 小区所在位置
    houseNumber = scrapy.Field() # 房屋链家编号

    # 房屋基本属性
    houseType = scrapy.Field() # 房屋户型
    houseFloor  = scrapy.Field() # 所在楼层
    houseBuildingArea = scrapy.Field() # 房屋建筑面积
    houseStructure = scrapy.Field() # 户型结构
    houseInnerArea = scrapy.Field() # 房屋套内面积
    houseBuildingType = scrapy.Field() # 建筑类型
    houseOrientation = scrapy.Field() # 房屋朝向
    houseBuildingStructure = scrapy.Field() # 建筑结构
    houseDecoration = scrapy.Field() # 装修情况
    houseElevatorRatio = scrapy.Field() # 梯户比例
    houseElevator = scrapy.Field() # 电梯配备
    housePrivilege = scrapy.Field() # 产权年限
    
    # 房屋交易属性
    houseListDate = scrapy.Field() # 挂牌时间
    houseTradeProperty = scrapy.Field() # 房屋交易权属
    houseLastTrade = scrapy.Field() # 上次交易时间
    houseUsage = scrapy.Field() # 房屋用途
    houseAgeLimit = scrapy.Field() # 房屋年限
    housePrivilegeProperty = scrapy.Field() # 产权所属
    housePledge = scrapy.Field() # 抵押信息
    houseRecord = scrapy.Field() # 房屋备案
    houseImg = scrapy.Field() # 房屋户型图

    # 爬虫关键信息
    houseUrl = scrapy.Field() # 房屋URL地址
    houseRefererUrl = scrapy.Field() # 房屋引用URL地址
    houseCrawlTime = scrapy.Field() # 爬取时间
