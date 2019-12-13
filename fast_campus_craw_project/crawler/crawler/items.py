import scrapy

class CrawlerItem(scrapy.Item):
    year = scrapy.Field()
    dates = scrapy.Field()
    times = scrapy.Field()
    results = scrapy.Field()
    parks = scrapy.Field()
    etcs = scrapy.Field()
