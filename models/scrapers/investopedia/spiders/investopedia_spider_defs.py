import scrapy
import json

from investopedia.items import InvestopediaItem

class InvestopediaSpiderDefs(scrapy.Spider):
    name = "investopedia"
    allowed_domains = ["investopedia.com"]




    with open('items.json', 'r') as f:
        x = json.loads(f.read())
    urls = set()
    for e in x:
      urls.add(e['link'])
    start_urls = list(urls)

    #start_urls = ["http://www.investopedia.com/terms/c/cdo2.asp"]

    def parse(self, response):
        # Find list items
        for sel in response.xpath('//div[@class="content-box content-box-term"]'):

            name = response.xpath('//h1/text()')[0].extract().strip()
            content = sel.xpath('p/text()')[0].extract().strip()
            content = sel.xpath('/html/head/meta[@name="description"]/@content')[0].extract().strip()
            if content != "":

                related = []
                for s2 in response.xpath('//div[@class="related-carousel-table"]/ol/li/h3[@class="item-title"]'):
                    url = s2.xpath('a/@href')[0].extract().strip()
                    rname = s2.xpath('a/text()')[0].extract().strip()
                    if rname != "":
                        url = response.urljoin(url)
                        print("Related: %s" % rname)
                        related.append(url)

                print(name)
                print(content)
                print(related)

                item = InvestopediaItem()
                item['name'] =  name
                item['related'] =  related
                item['description'] =  content
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
