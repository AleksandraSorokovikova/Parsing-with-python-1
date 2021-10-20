from scrapy.selector import Selector
import scrapy
import logging
from scrapy.crawler import CrawlerProcess

class cianSpider(scrapy.Spider):

    start_urls = []
    parsed_data = []
    name = "cian"

    custom_settings = {
        'LOG_LEVEL': logging.WARNING
    }

    def __init__(self, html_list, to_save, *args, **kwargs):
        self.start_urls = html_list
        self.parsed_data = to_save
        super(cianSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        for obj in response.xpath("//article[@data-name='CardComponent']"):
            line = {
                'name': Selector(text=obj.get()).xpath("//span[@data-mark='OfferTitle']/span/text()").get(),
                'price': Selector(text=obj.get()).xpath("//span[@data-mark='MainPrice']/span/text()").get(),
                'location': Selector(text=obj.get()).xpath("//a[@data-name='GeoLabel']/text()").getall(),
                }
            self.parsed_data.append(line)
            yield line
