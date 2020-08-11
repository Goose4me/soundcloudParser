import scrapy
from scrapy.http import Request


class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['soundcloud.com']
    start_urls = ['']

    @staticmethod
    def parse_playlist(response):
        songs = {}
        length = len(response.xpath('//noscript/article[1]/section[@class="tracklist"]/article').getall())
        for i in range(length):
            song = str(response.xpath('//noscript/article[1]/section[@class="tracklist"]/article[' + str(
                i + 1) + ']/h2[1]/a[1]/text()').get())
            author = str(response.xpath('//noscript/article[1]/section[@class="tracklist"]/article[' + str(
                i + 1) + ']/h2[1]/a[2]/text()').get())
            songs[str(author)] = str(song)
        return songs

    def parse(self, response):
        for link in response.xpath('//*/section/article/h2/a[1]/@href').extract():
            url = "https://soundcloud.com/" + link
            yield Request(url=url, callback=self.parse_playlist)
