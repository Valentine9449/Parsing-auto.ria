import scrapy


class AudioSpider(scrapy.Spider):
    name = 'audio'
    allowed_domains = ['www.amalgama-lab.com/']
    start_urls = ['http://www.amalgama-lab.com//']

    def parse(self, response):
        pass
