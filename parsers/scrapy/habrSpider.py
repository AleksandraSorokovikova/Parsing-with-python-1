from scrapy.selector import Selector
import scrapy
import logging
from scrapy.crawler import CrawlerProcess
from w3lib.html import strip_html5_whitespace as shw

class habrSpider(scrapy.Spider):

    start_urls = []
    parsed_data = []
    name = "habr"

    custom_settings = {
        'LOG_LEVEL': logging.WARNING
    }

    def __init__(self, html_list, to_save, *args, **kwargs):
        self.start_urls = html_list
        self.parsed_data = to_save
        super(habrSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        line = {
            'time': shw(response.xpath("//span[@class='tm-article-snippet__datetime-published']/time/@datetime").get()),
            'tags': [shw(result.lower())
                         for result in response.xpath("//a[@class='tm-tags-list__link']/text()").getall()],
            'habs': [shw(result.lower())
                         for result in response.xpath("//a[@class='tm-hubs-list__link']/text()").getall()],
            'saved': shw(response.xpath("//span[@class='bookmarks-button__counter']/text()").get()),
        }
        self.parsed_data.append(line)
        yield line
