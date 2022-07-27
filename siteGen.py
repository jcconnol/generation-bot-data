#TODO generate text list and add to lists directory

import requests
from bs4 import BeautifulSoup
import random
import re

SCRAPE_SITEMAP_URL = "https://www.ramseysolutions.com/articles/sitemap.xml"
BASE_URL = "https://www.ramseysolutions.com"
URL_LIMIT = 25

def buildMarkovSiteObject():
    response = requests.get(SCRAPE_SITEMAP_URL)    
    sitemap_xml = BeautifulSoup(response.text, 'xml')
    
    namespace = sitemap_xml.find('urlset').namespace    
    locs = sitemap_xml.select('default|loc', namespaces={'default': namespace})
    
    page_urls = []
    for loc in locs:
        page_urls.append(loc.get_text())
    
    random_pages = []
    for index in range(10):
        random_loc = random.randint(0, len(page_urls))
        random_pages.append(page_urls[random_loc])
    
    #TODO get all text from paragraphs and add to text file
    paragraph_text = ""
    print(random_pages)
    for page in random_pages:
        print(page)
        print(getPageParagraphText(page))
        paragraph_text += getPageParagraphText(page)
    
    print("writing")
    with open('lists/siteList.txt', 'w') as f:
        f.write(paragraph_text)
    
    
def getPageParagraphText(URL):
    paragraph_string = ""
    page_html = requests.get(URL).text
    htmlParse = BeautifulSoup(page_html, 'html.parser')
    
    # getting all the paragraphs
    for para in htmlParse.body.main.find_all("p"):
        print(para.get_text())
        paragraph_string += '\n\n' + para.get_text()
    
    return paragraph_string
    
if __name__=="__main__":
    buildMarkovSiteObject()