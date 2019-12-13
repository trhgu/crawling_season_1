from .mongodb import collection

class CrawlerPipeline(object):
    
    def process_item(self, item, spider):
        
        data = { "year": item["year"],
                 "dates": item["dates"], 
                 "times": item["times"],
                 "results": item["results"], 
                 "parks": item["parks"],
                 "etcs": item["etcs"],
               }
        
        collection.insert(data)
        
        return item
