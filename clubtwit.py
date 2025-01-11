import os
import requests
from lxml import etree
from dotenv import load_dotenv

class ClubTwit:
    def __init__(self):
        load_dotenv()
        self.clubtwit = os.getenv('twitcluburl')
        self.r = requests.get(self.clubtwit)
        self.clubtwitxml = etree.fromstring(bytes(self.r.text, 'utf-8'))
        self.shows = []
        self.items = self.clubtwitxml.findall('.//item')
        for self.item in self.items:
            self.title = self.item.find('title').text
            self.media = self.item.find('enclosure')
            self.link = self.media.attrib['url']
            self.length = self.media.attrib['length']
            self.pubDate = self.item.find('pubDate').text
            self.show={'Title':self.title,'Link':self.link,'PubDate':self.pubDate, 'Length':int(self.length)}
            self.shows.append(self.show)
