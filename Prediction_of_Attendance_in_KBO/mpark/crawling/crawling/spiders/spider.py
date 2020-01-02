import requests
import pandas as pd
import scrapy

from bs4 import BeautifulSoup
from scrapy.http import TextResponse
from crawling.items import CrawlingItem


class Spider(scrapy.Spider):
    name = "BaseballData"
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
        }
    }
    
    def start_requests(self):
        number = pd.read_csv("~/Documents/dev/craw/url_number.csv")
        for num in number["url"].values:
            url = "http://mlbpark.donga.com/mp/b.php?p={}&m=list&b=kbotown&query=&select=&user=".format(num)
            yield scrapy.Request(url, callback=self.page_content)

    def page_content(self, response):
        item = CrawlingItem()
        for i in range(4, 34, 3):
            t = '//*[@id="container"]/div[2]/div[1]/div[1]/table/tbody/tr[{}]/td/a/span/text()'.format(i)
            d = '//*[@id="container"]/div[2]/div[1]/div[1]/table/tbody/tr[{}]/td[4]/span/text()'.format(i)
            try:
                item["team"] = response.xpath(t)[0].extract()
            except:
                item["team"] = None
            item["date"] = response.xpath(d)[0].extract()
            yield item
