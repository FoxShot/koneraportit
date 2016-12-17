#!python

from lxml import html
import requests

page = requests.get('http://naurunappula.com/videot/')
tree = html.fromstring(page.content)

print tree
