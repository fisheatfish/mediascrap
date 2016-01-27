__author__ = 'grobvincent'



from pymongo import MongoClient




global links


client = MongoClient('localhost', 27017)
db = client.Medias

links = db.links

#, { "_id":0,"liste_links": 1}

#cursor = links.find({"name" : "http://chokomag.com/"},{ "_id" : 0 ,"liste_links" : 1})
cursor = links.find({"name":"http://www.rtl.fr/"},{"_id":0,"name":1,"liste_links":1})


for document in cursor:
    links = document


liste_links = links['liste_links']
start_links = links['name']

print(start_links)
global liste_links

global start_links



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

    name = "rtl"
    #allowed_domains =[start_links[8:21]]
    start_urls =liste_links
    rules = [
        #site which should be saved
        Rule(
            LinkExtractor(
                allow = ['/(\d+|\w+)']),
                'parse_page')]


    def parse_page(self,response):
        hxs = HtmlXPathSelector(response)


        #For rtl //div[@id="article-section"]/p//text()
        #For lemonde //div[@id="articleBody"]/p//text()
        #For liberation //div[@class="article-body read-left-padding"]/p//text()
        #For ma ville //div[@class="elmt-detail article"]/p//text()
        #For sud ouest //div[@class="entry-content"]/p//text()

        date_article = ''.join(hxs.select('//time[@class="item publish-time"]').extract()).strip()
        body = ''.join(hxs.select('//div[@id="article-section"]/p//text()').extract()).strip()


        item = NewsItem()

        if len(body)> 0 :
            item['site'] = start_links
            item['body'] = body
            item['url'] = response.url
            item['timeOfScrap'] = datetime.datetime.now()
            if len(date_article)>0 :
                item['date_article'] = date_article[42:67]
            return item


        else :
            pass
