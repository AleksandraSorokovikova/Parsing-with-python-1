import scrapy
from scrapy.crawler import CrawlerProcess

def parse_scrapy(spider, html_source_list, result):

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(spider, html_source_list, result)
    process.start()

