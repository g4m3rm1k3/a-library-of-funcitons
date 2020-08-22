import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from lxml import html
from cssselect import GenericTranslator, SelectorError

load_dotenv()
IMDB_URL = os.getenv('IMDB_URL')

r = requests.get(IMDB_URL)
if r.status_code == 200:
	tree = html.fromstring(r.content)
	movie = tree.xpath('//h3[@class="lister-item-header"]//a[starts-with(@href, "/")]/text()')
	year = tree.xpath('//h3[@class="lister-item-header"]//span[contains(@class, "lister-item-year")]/text()')
	placement = tree.xpath('//h3[@class="lister-item-header"]//span[contains(@class,"text-primary")]/text()')
else:
	print(f'There was an error connecting to the URL. Status code: {r.status_code}')


