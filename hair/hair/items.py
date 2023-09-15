# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HairItem(scrapy.Item):
    # Ad info
    ad_name = scrapy.Field()
    price = scrapy.Field()
    hair_length = scrapy.Field()
    hair_thickness = scrapy.Field()
    hair_color = scrapy.Field()
    gender = scrapy.Field()
    hair_ethnicity = scrapy.Field()
    hair_texture = scrapy.Field()
    hair_cut_by = scrapy.Field()
    hair_weight = scrapy.Field()
    country = scrapy.Field()
    zip_code = scrapy.Field()
    # Spider info
    url = scrapy.Field()
    spider = scrapy.Field()
    scraping_date = scrapy.Field()
