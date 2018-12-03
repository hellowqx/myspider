from scrapy_redis.spiders import RedisSpider
from ..settings import REDIS_URL

class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    # start_urls=['https://search.51job.com/list/000000%252C00,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']
    redis_key = 'myspider:start_urls'


    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        alls=response.xpath("//div[@class='el']")
        for i in alls:
            yield {
                'name':i.xpath(".//p/span/a/@title").extract_first(),
                'salary': i.xpath(".//span[@class='t4']/text()").extract_first(),
            }

        next_page=response.xpath("//ul/li[@class='bk'][2]/a[text()='下一页']/@href").extract()[0]
        if next_page:
            print(next_page,11111111111111111111)
            yield response.follow(next_page,self.parse)

