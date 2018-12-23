import scrapy

from investopedia.items import InvestopediaItem

class InvestopediaSpider(scrapy.Spider):
    name = "investopedia"
    allowed_domains = ["investopedia.com"]


    start_urls = []
    # x = '1abcdefghijklmnopqrstuvwxyz'
    # for c in range(0, len(x)):
    #     for i in range(1,20):
    #         if i == 1:
    #             start_urls.append("http://www.investopedia.com/terms/%s" % x[c])
    #         else:
    #             start_urls.append("http://www.investopedia.com/terms/%s?page=%d" % (x[c], i))

    def parse(self, response):
        # Find list items
        response
        for sel in response.xpath('//h3[@class="item-title"]'):
            url = sel.xpath('a/@href')[0].extract().strip()
            name = sel.xpath('a/text()')[0].extract().strip()
            if name != "":
                url = response.urljoin(url)
                item = InvestopediaItem()
                item['name'] =  name
                item['link'] =  url
                yield item
            #
            # yield scrapy.Request(url, self.parse)

        # for sel in response.xpath('//p'):
        #     text = sel.xpath('text()')[0].extract()
        #     if text.startswith('This chart provides the 3-month moving total'):
        #         bolds = sel.xpath('b')
        #         item = ItJobsWatchItem()
        #         item['name'] = bolds[0].xpath('text()').extract()[0]
        #         item['category'] = bolds[1].xpath('text()').extract()[0]

        #         ext = response.xpath('//a[@class="navExternal"]')
        #         if ext:
        #             item['wiki'] = ext.xpath('@href')[0].extract()

        #

        # next_page = response.xpath('//a[@class="next"]/@href')
        # if next_page:
        #     url = response.urljoin(next_page[0].extract())
        #     yield scrapy.Request(url, self.parse)
