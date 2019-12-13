import scrapy
import requests
import json
from crawler.items import CrawlerItem

class Spider(scrapy.Spider):
    name = "KBO"

    def start_requests(self):
        year = ["2017", "2018", "2019"]
        month = ["03","04","05", "06", "07", "08", "09", "10"]
        team = ["SK", "HH", "WO", "HT", "SS", "LT", "OB", "LG","KT","NC"]
        for self.y in year:
            for m in month:
                for t in team:
                    url = "https://www.koreabaseball.com/ws/Schedule.asmx/GetScheduleList?leId=1&srIdList=0%2C9&seasonId={}&gameMonth={}&teamId={}".format(self.y, m, t)
                    yield scrapy.Request(url, callback=self.match_parse)
 
    def match_parse(self, response):
        item = CrawlerItem()
        for n in range(0,31):
            try:
                item["year"] = self.y
                item["dates"] = json.loads(response.body)["rows"][n]['row'][0]['Text'] #날짜
                time = json.loads(response.body)["rows"][n]['row'][1]['Text'] #시간
                item["times"] = time.replace("<b>", "").replace("</b>", "")
                result = json.loads(response.body)["rows"][n]['row'][2]['Text'] #경기결과
                item["results"] = result.replace('<span class="win">',' win ').replace('<span class="lose">',' lose ').replace('<span class="same">',' same ').replace('</span><span>',' ').replace('</span></em><span>',' ').replace('<span>','').replace('</span>','').replace('<em>','').replace('</em>','')
                item["parks"] = json.loads(response.body)["rows"][n]['row'][7]['Text']  #구장
                item["etcs"] = json.loads(response.body)["rows"][n]['row'][8]['Text'] #비고
                yield item
  
            except:
                break
