import scrapy

class Content(scrapy.Spider):
    name = 'content'
    start_urls = ['https://akcesoriameblowepoznan.pl/']

    def parse(self, response):

        h1_text = response.css('h1::text').getall()

        yield {
            'all_h1': h1_text[0],
        }