import scrapy


class Content(scrapy.Spider):
    name = 'content'

    #Dynamiczne wybieranie url
    def __init__(self, url=None, *args, **kwargs):
        super(Content, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        meta = self.meta_data(response)
        images = self.extract_images(response)

        yield {
            'image_urls': images,
            'page': response.url,
            'total_images': len(images),
            'meta_data': meta
        }

    #Ekstrakcja Title

    #Ekstrakcja Meta danych
    def meta_data(self, response):
        return {
            'title': response.css('title::text').get(),
            'description': response.css('meta[name="description"]::attr(content)').get(),
            'keywords': response.css('meta[name="keywords"]::attr(content)').get(),
            'og_title': response.css('meta[property="og:title"]::attr(content)').get(),
        }

    #Eksrakcja Tekstu

    #Ekstrakcja Obrazow
    def extract_images(self, response):
        # Zbierz wszystkie URLe obrazów
        image_urls = response.css('img::attr(src)').getall()

        # Konwertuj relatywne URLe na absolutne
        image_urls = [response.urljoin(url) for url in image_urls]
        return image_urls
