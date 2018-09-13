import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import Selector
from items import FrameItem

class ImageSpider(scrapy.Spider):
    name = "image"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

        papers = response.xpath('')
        for paper in papers:
            url = paper.xpath('').extract()[0]

            item = FrameItem(url)

            yield item

        next_page = Selector(response).re('')
        if next_page:
            yield scrapy.Request(url=next_page[0], callback=self.parse)


if __name__=='__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(ImageSpider)
    process.start()