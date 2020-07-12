#!/usr/bin/python3.7
import datetime
import requests
from bs4 import BeautifulSoup

class Scrape:
    def __init__(self):
        self.url=None

    def scrape(self):
        self.getTarget()
        html_doc=requests.get(self.url)
        soup=BeautifulSoup(html_doc.text, 'html.parser')
        text=soup.find(id='textlines').get_text()
        if text and (not text.isspace()):
            print(text)

    def getTarget(self):
        now=datetime.datetime.now()
        date_formated=now.strftime("%Y%m%d")
        self.url="http://www.calefactory.org/calendar/wc"+date_formated+".htm"

s=Scrape()
s.scrape()
