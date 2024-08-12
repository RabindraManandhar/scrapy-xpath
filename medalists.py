import scrapy


class MedalistsSpider(scrapy.Spider):
    name = "medalists"
    allowed_domains = ["widipedia.org"]
    start_urls = ["https://widipedia.org"]

    def parse(self, response):
        pass
