__author__ = 'Vincent'


from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from mediascrap.items import NewsItem



class ChokomagSpider(CrawlSpider):
    """
    A spider crawls domains (in accordance with some  rules we will define
    to collect all the pages that we wish to extract our LemondeItems instances
    from. Most of this crawling logic is provided by Scrapy in the CrawlSpider class, so we
    can extend this class when writing our first spider.
    """

    name = "chokomag"
    allowed_domains =["http://chokomag.com/"]
    start_urls =[
       "http://chokomag.com/"
    ]
    rules = [
        #site which should be saved
        Rule(
            LinkExtractor(

                allow=['/\d{5}/\w+/\w+/\w+']),
                callback = 'parse_page')]


    def parse_page(self,response):
        hxs = HtmlXPathSelector(response)
        body = ''.join(hxs.select('//div[@id="content"]/article/div/p/text()').extract()).strip()
        item = NewsItem()

        item['body'] = body
        item['url'] = response.url

        return item

