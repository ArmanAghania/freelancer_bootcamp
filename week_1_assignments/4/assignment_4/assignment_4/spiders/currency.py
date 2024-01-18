import scrapy
from scrapy.loader import ItemLoader
from assignment_4.items import CurrencyItem


class CurrencySpider(scrapy.Spider):
    name = "currency"
    allowed_domains = ["www.currencyremitapp.com"]
    start_urls = ["https://www.currencyremitapp.com/world-currency-symbols"]

    def parse(self, response, **kwargs):
        # Select each row in the table
        for row in response.css('table.hometable.table-bordered tbody tr'):
            loader = ItemLoader(item=CurrencyItem(), selector=row)
            loader.add_css('country', 'td:nth-child(2)::text')
            loader.add_css('currency', 'td:nth-child(3)::text')
            loader.add_css('code', 'td:nth-child(4)::text')
            loader.add_css('symbol', 'td:nth-child(5)::text')
            loader.add_css('flag_image_url', 'td:nth-child(1) img::attr(src)')

            yield loader.load_item()
