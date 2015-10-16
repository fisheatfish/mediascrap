__author__ = 'karimsayadi'


from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class libeSpider (CrawlSpider):


    name = "libe"
    allowed_domains = ["www.liberation.fr"]
    start_urls = [
        "http://www.liberation.fr"
    ]

    rules = [

        Rule(
            LinkExtractor(
                allow=['/(monde,\d+|futurs,\d+']
            )
        )

    ]