__author__ = 'Vincent'


from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from mediascrap.items import NewsItem
import datetime



class ChokomagSpider(CrawlSpider):
    """
    A spider crawls domains (in accordance with some  rules we will define
    to collect all the pages that we wish to extract our LemondeItems instances
    from. Most of this crawling logic is provided by Scrapy in the CrawlSpider class, so we
    can extend this class when writing our first spider.
    """

    name = "chokomag"
    allowed_domains =["chokomag.com"]
    start_urls =[
       "http://www.chokomag.com"
    ]
    rules = [
        #site which should be saved
        Rule(
            LinkExtractor(
                allow=['/\d+/']),
                'parse_page')]


    def parse_page(self,response):
        hxs = HtmlXPathSelector(response)
        body = ''.join(hxs.select('//div[@class="entry-content clearfix"]/p//text()').extract()).strip()
        item = NewsItem()
        if len(body)> 0 :
            item['body'] = body
            item['url'] = response.url
            item['timeOfScrap'] = datetime.datetime.now()

            return item
        else :
            pass
