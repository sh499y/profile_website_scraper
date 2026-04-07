import scrapy


class Content(scrapy.Spider):
    name = 'content'

    #Dynamiczne wybieranie url
    def __init__(self, url=None, *args, **kwargs):
        super(Content, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        images = self.extract_images(response)

        yield {
            'image_urls': images,
            'page': response.url,
            'total_images': len(images)
        }

    #Ekstrakcja Obrazow
    def extract_images(self, response):
        # Zbierz wszystkie URLe obrazów
        image_urls = response.css('img::attr(src)').getall()

        # Konwertuj relatywne URLe na absolutne
        image_urls = [response.urljoin(url) for url in image_urls]
        return image_urls