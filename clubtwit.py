import os
import requests
from dotenv import load_dotenv
from lxml import etree
from pprint import pprint
from io import StringIO


class ClubTwit:
    def __init__(self):
        load_dotenv()
        self.clubtwit = os.getenv("twitcluburl")
        self.r = requests.get(self.clubtwit)
        self.clubtwitxml = etree.fromstring(bytes(self.r.text, "utf-8"))
        self.shows = []
        self.items = self.clubtwitxml.findall(".//item")
        for self.item in self.items:
            self.title = self.item.find("title").text
            description = self.item.find("description").text
            parser = etree.HTMLParser()
            tree = etree.parse(StringIO(description), parser)
            first_p = tree.xpath("//p[1]")
            if first_p:
                self.description = first_p[0].text
            else:
                self.description = ""
            self.media = self.item.find("enclosure")
            self.link = self.media.attrib["url"]
            self.length = self.media.attrib["length"]
            self.pubDate = self.item.find("pubDate").text
            self.show = {
                "Title": self.title,
                "Description": self.description,
                "Link": self.link,
                "PubDate": self.pubDate,
                "Length": int(self.length),
            }
            self.shows.append(self.show)
        pprint(self.shows)
