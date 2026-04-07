import scrapy


class Content(scrapy.Spider):
    name = 'content'
    
    def __init__(self, url=None, *args, **kwargs):
        super(Content, self).__init__(*args, **kwargs)
        
        if url:
            self.start_urls = [url]
        else:
            # Domyślny URL jeśli nie podano
            print("Link ERROR")
    
    def parse(self, response):
        # Zbierz wszystkie URLe obrazów
        image_urls = response.css('img::attr(src)').getall()
        
        # Konwertuj relatywne URLe na absolutne
        image_urls = [response.urljoin(url) for url in image_urls]
        
        yield {
            'image_urls': image_urls,
            'page': response.url,
            'total_images': len(image_urls)
        }