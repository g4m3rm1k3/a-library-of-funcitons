from lxml import html
import requests

page = requests.get('https://www.brainyquote.com/topics/wisdom-quotes')
tree = html.fromstring(page.content)
quotes = tree.xpath('//a[@title="view quote"]/text()')