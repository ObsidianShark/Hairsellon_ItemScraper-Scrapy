from datetime import datetime

import scrapy
from hair.items import HairItem
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst

class HairsellonSpider(scrapy.Spider):
    name = "hairsellon"
    allowed_domains = ["hairsellon.com"]
    start_urls = ["https://hairsellon.com/ads/"]

    custom_settings = {
        "AUTOTHROTTLE_ENABLED" : True,
        "AUTOTHROTTLE_DEBUG" : True,        
        }

    def parse(self, response):
        for link in response.xpath("//article/@data-permalink"):
            yield scrapy.Request(url=link.get(), callback=self.parse_ad)

        next_page = response.xpath("//a[@class='next page-numbers']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_ad(self, response):
        ad = ItemLoader(item=HairItem(), selector=response)
        ad.default_input_processor = MapCompose()
        ad.default_output_processor = TakeFirst()
        
        ad.add_xpath("ad_name", "//header/h1[@class='entry-title']/text()")
        ad.add_xpath("price", "//header/p[@class='entry-title cp_price']/text()")
        ad.add_xpath(
            "hair_length",
            "//section[@id='cp_widget_listing_custom_fields-1']//tr[@id='cp_hair_length']/td[2]/text()",
        )
        ad.add_xpath(
            "hair_thickness",
            "//section[@id='cp_widget_listing_custom_fields-1']//tr[@id='cp_hair_thickness']/td[2]/text()",
        )
        ad.add_xpath(
            "hair_color",
            "//section[@id='cp_widget_listing_custom_fields-1']//tr[@id='cp_hair_colour']/td[2]/text()",
        )
        ad.add_xpath(
            "gender",
            "//section[@id='cp_widget_listing_custom_fields-1']//tr[@id='cp_please_select'][td[contains(text(), 'Gender')]]/td[2]/text()",
        )
        ad.add_xpath(
            "hair_ethnicity", "//tr[@id='cp_your_nationalityhair_type']/td[2]/text()"
        )
        ad.add_xpath("hair_texture", "//tr[@id='cp_hair_texture']/td[2]/text()")
        ad.add_xpath("hair_cut_by", "//tr[@id='cp_hair_to_be_cut_by']/td[2]/text()")
        ad.add_xpath("hair_weight", "//tr[@id='cp_hair_weight']/td[2]/text()")
        ad.add_xpath("country", "//tr[@id='cp_country']/td[2]/text()")
        ad.add_xpath("zip_code", "//tr[@id='cp_zipcode']/td[2]/text()")

        ad.add_value("url", response.request.url)
        ad.add_value("spider", self.name)
        ad.add_value("scraping_date", datetime.now())

        yield ad.load_item()
