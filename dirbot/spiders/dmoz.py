from scrapy.spider import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    #allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.lequipe.fr/Football/FootballFicheClub77.html",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        #sites = sel.xpath('//table//tr/td')
        items = []

        #item['country'] = sel.xpath('/body/div/div/section/div/div/div/table//tr/td/span/text()').extract()

        #for i in range(0,1):
        
        

        for i in range(0,len(sel.xpath('.//table[@id="club_effectif_club"]//tr/td/a/text()').extract())):
            item = Website()
            item['name'] = sel.xpath('//table[@id="club_effectif_club"]//tr/td/a/text()').extract()[i]
            item['country'] = sel.xpath('//table[@id="club_effectif_club"]//tr/td[span][1]/text()').extract()[2*i+1]
            item['club'] = sel.xpath('.//body/@club').extract()
            items.append(item)


        return items

#http://www.lequipe.fr/Football/FootballFicheClub71.html/body/div[5]/div[2]/section[3]/div[1]/div/div[2]/table//tr[1]/td[2]
