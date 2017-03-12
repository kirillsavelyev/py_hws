# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join


# class CustomPipeline(object):
# 	def process_item(self, item, spider):
# 		if isinstance(item, BlogCategory):
# 			item['name'] = 'URL: ' + item['name']
# 		return item


class BlogCategory(scrapy.Item):
	hub = scrapy.Field(output_processor=TakeFirst())
	text = scrapy.Field(output_processor=TakeFirst())
	title = scrapy.Field(output_processor=TakeFirst())
	url = scrapy.Field(output_processor=Join())


class BlogSpider(scrapy.Spider):
	"""docstring for BlogSpider"""
	name = 'blogspider'
	start_urls = ['https://habrahabr.ru']

	# custom_settings = {
	# 	'ITEM_PIPELINES': {
	# 		'spider.CustomPipeline': 1
	# 	}
	# }

	def parse(self, responce):
		for url in responce.css('.post__title_link::attr("href")'):
		# for url in responce.xpath('//li[re:test(@class, "item-\d$")]//@href').extract():
			yield scrapy.Request(responce.urljoin(url), self.parce_article(url))

	def parse_article(self, responce, url):
		loader = ItemLoader(item=BlogCategory(), response=responce)
		loader.add_value('url', url)
		loader.add_css('title', 'h1.post__title span::text')
		loader.add_css('text', 'div.content html_format::text')
		loader.add_css('hub', 'div.hubs::text')
		yield loader.load_item()
