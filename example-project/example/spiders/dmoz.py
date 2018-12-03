from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = ["https://search.51job.com/list/000000%252C00,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="]

    rules = [
        Rule(LinkExtractor(restrict_css=('.bk a')),callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):
        for div in response.css('.el'):
            yield {
                'name': div.css('.t1 a::text').extract_first().strip(),
                'link': div.css('.t2 a::attr(href)').extract_first().strip(),
                'time': div.css('.t5::text').extract_first().strip(),
            }
