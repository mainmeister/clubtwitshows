import os
import requests
from dotenv import load_dotenv
from lxml import etree
from io import StringIO
import logging

# Set up basic logging to warn us of issues instead of crashing
logging.basicConfig(level=logging.INFO)

class ClubTwit:
    def __init__(self):
        """Initializes the class and loads the environment variable."""
        load_dotenv()
        self.clubtwit_url = os.getenv("twitcluburl")
        self.shows = []
        
        # Check if the URL was found in the environment variables
        if not self.clubtwit_url:
            raise ValueError("Environment variable 'twitcluburl' is not set.")
            
        # Automatically fetch the shows when the object is created
        self._fetch_and_parse_shows()

    def _fetch_and_parse_shows(self):
        """Fetches the XML feed from the URL and parses the show data."""
        # Security/Robustness: Add a timeout of 10 seconds to prevent hanging
        try:
            response = requests.get(self.clubtwit_url, timeout=10)
            response.raise_for_status()  # Check for HTTP errors (like 404 or 500)
        except requests.RequestException as e:
            logging.error(f"Failed to fetch data from Club Twit: {e}")
            return

        # Efficiency: Use response.content (raw bytes) instead of encoding text
        clubtwitxml = etree.fromstring(response.content)
        
        # Efficiency: Instantiate the HTML parser ONCE outside the loop
        html_parser = etree.HTMLParser()

        items = clubtwitxml.findall(".//item")
        
        # PEP 8: Use local variables (e.g., 'item', 'title') instead of 'self.item'
        for item in items:
            # Robustness: Safely get text in case the tag is missing
            title_element = item.find("title")
            title = title_element.text if title_element is not None else "Unknown Title"
            
            description_element = item.find("description")
            description_raw = description_element.text if description_element is not None else ""
            
            # Parse the HTML inside the description to get the first paragraph
            description_text = ""
            if description_raw:
                tree = etree.parse(StringIO(description_raw), html_parser)
                first_p = tree.xpath("//p[1]")
                if first_p and first_p[0].text:
                    description_text = first_p[0].text

            # Robustness: Safely extract media attributes
            media = item.find("enclosure")
            if media is not None:
                link = media.get("url", "")
                length_str = media.get("length", "0")
            else:
                link = ""
                length_str = "0"
                
            pub_date_element = item.find("pubDate")
            pub_date = pub_date_element.text if pub_date_element is not None else ""

            # Build the dictionary for this show
            show = {
                "Title": title,
                "Description": description_text,
                "Link": link,
                "PubDate": pub_date,
                "Length": int(length_str) if length_str.isdigit() else 0,
            }
            
            self.shows.append(show)