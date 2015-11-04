__author__ = 'grobvincent'


from scrapy.spider         import BaseSpider
from scrapy.selector         import HtmlXPathSelector
from mediascrap.items        import NettutsItem
from scrapy.http        import Request



class MySpider(BaseSpider):
    name         = "nettuts"
    allowed_domains    = ["net.tutsplus.com"]
    start_urls    = ["http://net.tutsplus.com/"]

    def parse(self, response):

        hxs     = HtmlXPathSelector(response)
        titles     = hxs.select('//h1[@class="post_title"]/a/text()').extract()

        for title in titles :
            item = NettutsItem()
            item["title"] = title
            yield item



