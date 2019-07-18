# -*- coding: utf-8 -*-

# Scrapy settings for crawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'crawl'

SPIDER_MODULES = ['crawl.spiders']
NEWSPIDER_MODULE = 'crawl.spiders'


ITEM_PIPELINES = {
    'crawl.pipelines.MysqlPipeline':100
}

LOG_LEVEL = 'ERROR'
LOG_FILE = 'scrapy.log'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True
USER_AGENT = "Baiduspider"


