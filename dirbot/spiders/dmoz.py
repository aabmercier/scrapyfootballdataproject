from scrapy.spider import Spider
from scrapy.selector import Selector

from dirbot.items import Website

from scrapy.http import Response

class DmozSpider(Spider):
    name = "dmoz"
    #allowed_domains = ["dmoz.org"]
    start_urls = [
        #"http://www.lequipe.fr/Football/",
        "http://www.lequipe.fr/Football/EQ_ANG.html"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        
        items = []


        urls = response.selector.xpath('//div[@id="container"]/div[@id="col-gauche"]/section/div[2]/ul/li/div[@class="club-left"]/a/@href').extract()

        for i in range(0,len(urls)):
            urls[i] = 'http://www.lequipe.fr'.join(urls[i].encode('utf8'))



            
        for i in range(0,len(urls)):
            res = Response(url = urls[i])
            for i in range(0,len(Selector(response = res).xpath('.//table[@id="club_effectif_club"]//tr/td/a/text()').extract())):
                item = Website()
                item['name'] = res.selector.xpath('//table[@id="club_effectif_club"]//tr/td/a/text()').extract()[i]
                item['country'] = res.selector.xpath('//table[@id="club_effectif_club"]//tr/td[span][1]/text()').extract()[2*i+1]
                item['club'] = res.selector.xpath('.//body/@club').extract()
                items.append(item)

        return items


