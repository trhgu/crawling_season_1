import scrapy

class CrawlingItem(scrapy.Item):
    team = scrapy.Field()
    date = scrapy.Field()
