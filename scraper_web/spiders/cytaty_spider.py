import scrapy


class CytatySpider(scrapy.Spider):
    name = 'cytaty'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        """Pobiera cytaty ze strony"""
        for quote in response.css('div.quote'):
            yield {
                'tekst': quote.css('span.text::text').get(),
                'autor': quote.css('small.author::text').get(),
                'tagi': quote.css('div.tags a.tag::text').getall(),
            }

        # Przejdź do następnej strony
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
