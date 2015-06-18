from scrapy.item import Item, Field


class Website(Item):

    name = Field()
    country = Field()
    club = Field()
    url= Field()
    #age = Field()
