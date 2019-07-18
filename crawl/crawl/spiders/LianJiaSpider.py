#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created author:tianxing
# created date:2018-05-30

import scrapy
import random
import datetime
import re
from crawl.items import House

class LianjiaSpider(scrapy.Spider):
    # 爬虫名称，爬虫时执行scrapy crawl lianjia
    name = 'lianjia'

    start_urls = []
    
    for page in range(1,101):
        start_urls.append('https://cd.lianjia.com/ershoufang/pg' + str(page) + '/')
    
    # 随机排序
    random.shuffle(start_urls)

    def parse(self,response):
        Links = response.xpath('//ul[@class="sellListContent"]/li')

        for url in Links:
            item = House()
            # 引用URL地址
            item['houseRefererUrl'] = response.url

            singleUrl = url.xpath('div[@class="info clear"]/div[@class="title"]/a/@href').extract()[0]
            
            # 向子页面发出请求
            yield scrapy.Request(url=singleUrl,meta={'item':item},callback=self.parse_page)

    def parse_page(self,response):
        item = response.meta['item']

        # 房屋基本信息，房屋标题、房屋总价、房屋单价、房屋首付、房屋税费、小区名称、小区所在位置、房屋链家编号
        # 房屋标题
        try:
            item['houseTitle'] = response.xpath('//div[@class="content"]/div[@class="title"]/h1/text()').extract()[0].strip()
        except:
            item['houseTitle'] = ''
        
        # 房屋总价
        try:
            # 数值
            houseTotalMoneyNum = response.xpath('//div[@class="price "]/span[@class="total"]/text()').extract()[0].replace(' ','')
            # 单位
            houseTotalMoneyUnit = response.xpath('//div[@class="price "]/span[@class="unit"]/span/text()').extract()[0].replace(' ','')
            item['houseTotalMoney'] =  houseTotalMoneyNum + houseTotalMoneyUnit
        except:
            item['houseTotalMoney'] = ''
        
        # 房屋单价
        try:
            houseSinglePrice = response.xpath('//span[@class="unitPriceValue"]')
            item['houseSinglePrice'] = houseSinglePrice.xpath('string(.)').extract()[0].replace(' ','')
        except:
            item['houseSinglePrice'] = ''

        # 房屋首付
        try:
            item['houseDownPayment'] =  re.findall(r'<span class="taxtext" title="首付(.+?) 税费">', response.text)[0]
        except:
            item['houseDownPayment'] = ''
        
        # 小区名称
        try:
            item['houseGardenName'] = response.xpath('//div[@class="aroundInfo"]/div[@class="communityName"]/a[1]/text()').extract()[0].replace(' ','')
        except:
            item['houseGardenName'] = ''
        
        # 小区所在位置
        try:
            houseLocation = response.xpath('//div[@class="aroundInfo"]/div[@class="areaName"]/span[@class="info"]')
            item['houseLocation'] = houseLocation.xpath('string(.)').extract()[0].strip().replace('\xa0','\t')
        except:
            item['houseLocation'] = ''
        
        # 房屋链家编号
        try:
            item['houseNumber'] = response.xpath('//div[@class="aroundInfo"]/div[@class="houseRecord"]/span[2]/text()').extract()[0].replace('"','')
        except:
            item['houseNumber'] = ''

        # 房屋基本信息，房屋户型、房屋所在楼层、建筑面积、户型结构、套内面积、建筑类型、房屋朝向、建筑结构、装修情况、梯户比例、配备电梯、产权年限
        # 基本属性的基准xpath
        baseXpath = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]/ul')
        
        # 房屋户型
        try:
            item['houseType'] = baseXpath.xpath('li[1]/text()').extract()[0].replace(' ','')
        except:
            item['houseType'] = ''

        # 所在楼层
        try:
            item['houseFloor'] = baseXpath.xpath('li[2]/text()').extract()[0].replace(' ','')
        except:
            item['houseFloor'] = ''
        
        # 房屋建筑面积
        try:
            item['houseBuildingArea'] = baseXpath.xpath('li[3]/text()').extract()[0].replace(' ','')
        except:
            item['houseBuildingArea'] = ''
        
        # 户型结构
        try:
            item['houseStructure'] = baseXpath.xpath('li[4]/text()').extract()[0].replace(' ','')
        except:
            item['houseStructure'] = ''
        
        # 房屋套内面积
        try:
            item['houseInnerArea'] = baseXpath.xpath('li[5]/text()').extract()[0].replace(' ','')
        except:
            item['houseInnerArea'] = ''
        
        # 建筑类型
        try:
            item['houseBuildingType'] = baseXpath.xpath('li[6]/text()').extract()[0].replace(' ','')
        except:
            item['houseBuildingType'] = ''
        
        # 房屋朝向
        try:
            item['houseOrientation'] = baseXpath.xpath('li[7]/text()').extract()[0].replace(' ','')
        except:
            item['houseOrientation'] = ''

        # 建筑结构
        try:
            item['houseBuildingStructure'] = baseXpath.xpath('li[8]/text()').extract()[0].replace(' ','')
        except:
            item['houseBuildingStructure'] = ''
        
        # 装修情况
        try:
            item['houseDecoration'] = baseXpath.xpath('li[9]/text()').extract()[0].replace(' ','')
        except:
            item['houseDecoration'] = ''

        # 梯户比例
        try:
            item['houseElevatorRatio'] = baseXpath.xpath('li[10]/text()').extract()[0].replace(' ','')
        except:
            item['houseElevatorRatio'] = ''
        
        # 电梯配备
        try:
            item['houseElevator'] = baseXpath.xpath('li[11]/text()').extract()[0].replace(' ','')
        except:
            item['houseElevator'] = ''
        
        # 产权年限
        try:
            item['housePrivilege'] = baseXpath.xpath('li[12]/text()').extract()[0].replace(' ','')
        except:
            item['housePrivilege'] = ''

        # 房屋交易信息，挂牌时间、交易权属、上次交易、房屋用途、房屋年限、产权所属、抵押信息、房屋备案
        # 交易属性的基准xpath
        transXpath = response.xpath('//div[@class="introContent"]/div[@class="transaction"]/div[@class="content"]/ul')
        
        # 挂牌时间
        try:
            item['houseListDate'] = transXpath.xpath('li[1]/span[2]/text()').extract()[0].replace(' ','')
        except:
            item['houseListDate'] = ''
        
        # 交易权属
        try:
            item['houseTradeProperty'] = transXpath.xpath('li[2]/span[2]/text()').extract()[0].replace(' ','')
        except:
            item['houseTradeProperty'] = ''
        
        # 上次交易
        try:
            item['houseLastTrade'] = transXpath.xpath('li[3]/span[2]/text()').extract()[0].replace(' ','')
        except:
            item['houseLastTrade'] = ''
        
        # 房屋用途
        try:
            item['houseUsage'] = transXpath.xpath('li[4]/span[2]/text()').extract()[0].replace(' ','')
        except:
            item['houseUsage'] = ''
        
        # 房屋年限
        try:
            item['houseAgeLimit'] = transXpath.xpath('li[5]/span[2]/text()').extract()[0].replace(' ','')
        except:
            item['houseAgeLimit'] = ''
        
        # 产权所属
        try:
            item['housePrivilegeProperty'] = transXpath.xpath('li[6]/span[2]/text()').extract()[0].replace(' ','')
        except:
            item['housePrivilegeProperty'] = ''
        
        # 抵押信息
        try:
            item['housePledge'] = transXpath.xpath('li[7]/span[2]/text()').extract()[0].replace(' ','').replace('\n','')
        except:
            item['housePledge'] = ''
        
        # 房屋备案
        try:
            item['houseRecord'] = transXpath.xpath('li[8]/span[2]/text()').extract()[0].replace(' ','')
        except:
            item['houseRecord'] = ''

        # 房屋户型图
        try:
            item['houseImg'] = response.xpath("//div[@class='imgdiv']/img/@src").extract()[0].replace("240x180","533x400")
        except:
            item['houseImg'] = ''

        # 爬虫关键信息
        # 房屋URL地址
        item['houseUrl'] = response.url

        # 房屋爬虫时间
        item['houseCrawlTime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # 实际要取得内容
        yield item