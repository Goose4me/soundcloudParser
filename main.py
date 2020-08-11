from soundcloudParser.spider import MainSpider
from scrapy.crawler import CrawlerProcess
import os
settings = {
'FEED_FORMAT': 'json',
'FEED_URI': 'result.json'
}
if settings.get("FEED_URI") in os.listdir():
    with open(settings.get("FEED_URI"), "w" ) as f:
        f.write("")
process = CrawlerProcess(settings)
url = "https://soundcloud.com/goose-gas/sets"
process.crawl(MainSpider, start_urls=[url])
process.start()
