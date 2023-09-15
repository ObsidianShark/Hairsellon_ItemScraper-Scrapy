from itemloaders.processors import Join, MapCompose, TakeFirst
from scrapy.loader import ItemLoader


class HairLoader(ItemLoader):
    default_input_processor = MapCompose()
    default_output_processor = TakeFirst()
