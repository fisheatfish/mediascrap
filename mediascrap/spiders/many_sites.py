from pymongo import MongoClient




global links


client = MongoClient('localhost', 27017)
db = client.Medias

links = db.links

#, { "_id":0,"liste_links": 1}

cursor = links.find({"name" : "http://chokomag.com/"},{ "_id" : 0 ,"liste_links" : 1})

links = 0


for document in cursor:
    links = document

print(links)

links = links['liste_links']

print(links)

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

    name = "many_sites"
    allowed_domains =["chokomag.com"]
    start_urls =links
    rules = [
        #site which should be saved
        Rule(
            LinkExtractor(
                allow = ['/(\d+|\w+)']),
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
