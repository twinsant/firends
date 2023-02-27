import scrapy


class FirendsSpider(scrapy.Spider):
    name = "friends"
    allowed_domains = ["fangj.github.io"]
    start_urls = ["https://fangj.github.io/friends/"]

    def parse(self, response):
        all = response.xpath('//a')
        for a in all:
            next_page = a.attrib['href']
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse_page)

    def parse_page(self, response):
        yield {
            'title': response.xpath('//title/text()').extract_first(),
            'url': response.url,
        }
