# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import datetime,json,logging,pymysql.cursors
import pymongo
from scrapy.conf import settings


logging.basicConfig(filename='scrapy.log')
logger = logging.getLogger(__name__)

class MysqlPipeline(object):

    def __init__(self):
        pass

    def open_spider(self, spider):
        self.mysql_conn = pymysql.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'root',
            db = 'temp',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        if 'house' == item.className:
            try:
                sql_search = "select houseTitle from `house` where `houseTitle`=%s"
                with self.mysql_conn.cursor() as cursor:
                    cursor.execute(sql_search, (item.get('houseTitle', '')))
                    houseIsExist = cursor.fetchone()
                    
                    if houseIsExist is None:
                        sql_write = "insert into `house` (`houseId`, `houseTitle`, `houseTotalMoney`, `houseSinglePrice`, `houseDownPayment`, `houseGardenName`,\
                        `houseLocation`, `houseNumber`, `houseType`, `houseFloor`, `houseBuildingArea`, `houseStructure`, \
                        `houseInnerArea`, `houseBuildingType`, `houseOrientation`, `houseBuildingStructure`, `houseDecoration`, `houseElevatorRatio`, \
                        `houseElevator`, `housePrivilege`, `houseListDate`, `houseTradeProperty`, `houseLastTrade`, `houseUsage`, \
                        `houseAgeLimit`, `housePrivilegeProperty`, `housePledge`, `houseRecord`, `houseImg`, `houseUrl`, `houseRefererUrl`, `houseCrawlTime`) \
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                        cursor.execute(sql_write, (0, item.get('houseTitle', ''), item.get('houseTotalMoney', ''), item.get('houseSinglePrice', '') \
                        , item.get('houseDownPayment', ''), item.get('houseGardenName', ''), item.get('houseLocation', ''), item.get('houseNumber', '') \
                        , item.get('houseType', ''), item.get('houseFloor', ''), item.get('houseBuildingArea', ''), item.get('houseStructure', '') \
                        , item.get('houseInnerArea', ''), item.get('houseBuildingType', ''), item.get('houseOrientation', ''), item.get('houseBuildingStructure', '') \
                        , item.get('houseDecoration', ''), item.get('houseElevatorRatio', ''), item.get('houseElevator', ''), item.get('housePrivilege', '') \
                        , item.get('houseListDate', ''), item.get('houseTradeProperty', ''), item.get('houseLastTrade', ''), item.get('houseUsage', '') \
                        , item.get('houseAgeLimit', ''), item.get('housePrivilegeProperty', ''), item.get('housePledge', ''), item.get('houseRecord', '') \
                        , item.get('houseImg', ''), item.get('houseUrl', ''), item.get('houseRefererUrl', ''), item.get('houseCrawlTime', '')))

                self.mysql_conn.commit()
                
            except Exception as e:
                logger.error(item.get('houseUrl',''))
                logger.error(e)
                logger.error('---------------------------------------\n')
        return item

    def close_spider(self, spider):
        self.mysql_conn.close()
