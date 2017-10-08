# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class ScrapyDaomuItem(Item):
    book_name = Field()
    chapter_num = Field()
    chapter_name = Field()
    chapter_url = Field()
