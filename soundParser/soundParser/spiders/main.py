# -*- coding: utf-8 -*-
import scrapy


class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['soundcloud.com']
    start_urls = ['https://soundcloud.com/goose-gas/sets/aaaaa']

    def parse(self, response):
        songs = {}
        length = len(response.xpath('//noscript/article[1]/section[@class="tracklist"]/article').getall())
        for i in range(length):
            song = str(response.xpath('//noscript/article[1]/section[@class="tracklist"]/article['+str(i+1)+']/h2[1]/a[1]/text()').get())
            author = str(response.xpath('//noscript/article[1]/section[@class="tracklist"]/article['+str(i+1)+']/h2[1]/a[2]/text()').get())
            songs[str(author)] = str(song)
        print()
        print()
        print()
        print(songs)
