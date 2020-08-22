import requests   
from bs4 import BeautifulSoup
from lxml import html
from cssselect import GenericTranslator, SelectorError

r = requests.get('https://www.imdb.com/list/ls055592025/')
tree = html.fromstring(r.content)
movie = tree.xpath('//h3[@class="lister-item-header"]//a[starts-with(@href, "/")]/text()')
year = tree.xpath('//h3[@class="lister-item-header"]//span[contains(@class, "lister-item-year")]/text()')
placement = tree.xpath('//h3[@class="lister-item-header"]//span[contains(@class,"text-primary")]/text()')


