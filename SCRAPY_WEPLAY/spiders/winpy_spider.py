import scrapy
from SCRAPY_WEPLAY.items import ScrapyWeplayItem 

class WinpySpider(scrapy.Spider):
    name = 'winpy'
    custom_settings = { 'DOWNLOD_DELAY': 5 }
    allowed_domains = ['www.weplay.cl']

    # URL SECTION
    start_urls = [
        'https://www.weplay.cl/consolas/consolas-ps5.html', 
        'https://www.weplay.cl/consolas/consolas-switch.html',
        'https://www.weplay.cl/consolas/consolas-xbox-sx.html',
        'https://www.weplay.cl/consolas/consolas-xbox-one.html',
        'https://www.weplay.cl/consolas/consolas-xbox-360.html',
    ]

    def parse(self, response):
        
        quote_item = ScrapyWeplayItem()
        quote_item['title'] = response.xpath('//h1[@class="product-name"]/text()').get()
        quote_item['link'] = response.url
        quote_item['price'] = response.xpath('//span[@class="price"]/text()').get()
        quote_item['special_price'] = response.xpath('//span[@class="special-price"]/text()').get()
        yield quote_item

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
        
