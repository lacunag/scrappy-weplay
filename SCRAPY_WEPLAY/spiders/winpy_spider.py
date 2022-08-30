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
    ]

    def parse(self, response):
        
        quote_item = ScrapyWeplayItem()

        for title in response.css('.product-item-details'):
            
            quote_item['title'] = title.css('.product-item-link::text').get().strip()
            quote_item['link'] = title.css('::attr(href)').get()
            quote_item['price'] = title.css('.price::text').get()
            quote_item['special_price'] = title.css('.special-price .price ::text').get()
            yield quote_item

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
