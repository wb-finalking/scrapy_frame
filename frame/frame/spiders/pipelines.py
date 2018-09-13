import json
from scrapy.exceptions import DropItem

class NormalPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if item['']:
            pass
        else:
            raise DropItem('')