from urllib.error import URLError
from xml.etree.ElementTree import Comment
import scrapy

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
        'https://www.weplay.cl/consolas/consolas-ps3.html',
        'https://www.weplay.cl/consolas/consolas-ps4.html',
    ]

    def parse(self, response):
        for title in response.css('.product-item-details'):
            yield {'title': title.css('.product-item-link::text').get().strip(), 'link': title.css('::attr(href)').get(), 'price': title.css('.price::text').get(), 'special_price': title.css('.special-price .price ::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)

