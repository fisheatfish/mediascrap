__author__ = 'karimsayadi'

from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from mediascrap.items import NewsItem
import datetime



class LemondeSpider(CrawlSpider):
    """
    A spider crawls domains (in accordance with some  rules we will define
    to collect all the pages that we wish to extract our LemondeItems instances
    from. Most of this crawling logic is provided by Scrapy in the CrawlSpider class, so we
    can extend this class when writing our first spider.
    """

    name = "lemonde"
    allowed_domains =["www.lemonde.fr"]
    start_urls =[
        "http://www.lemonde.fr"
    ]
    rules = [
        #site which should be saved
        Rule(
            LinkExtractor(
                allow=['/(international|politique|societe|economie|culure|idee|planete|sport|sciences|pixels|compus)/article/\d{4}/\d{2}/\d{2}/\w+']),
                'parse_page')]



                #allow=('[\/\w-]/article/\d{4}/\d{2}/\d{2}/[\w-]?$')

    def parse_page(self,response):
        hxs = HtmlXPathSelector(response)

        body = ''.join(hxs.select('//div[@id="articleBody"]/p//text()').extract()).strip()
        item = NewsItem()

        if len(body)> 0 :
            item['body'] = body
            item['url'] = response.url
            item['timeOfScrap'] = datetime.datetime.now()

            return item
        else :
            pass
