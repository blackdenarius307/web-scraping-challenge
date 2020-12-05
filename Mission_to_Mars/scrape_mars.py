#Importations
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from splinter.exceptions import ElementDoesNotExist

#Start Browser
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

#Scraping
def scrape():
    browser = init_browser()
    
    #Set news scraping parameters
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Use the power of Soup to find what we're looking for
    titles_found = soup.find_all('div', class_='content_title', limit=2)
    paragraphs_found = soup.find_all('div', class_='article_teaser_body', limit=1)

    #Make some lists for our soup... Bowels, if you will
    headlines = []
    paragraphs= []

    #Plop the right kind of soup into the headlines bowel.
    for title in titles_found:
        if (title.a):
            if(title.a.text):
                headlines.append(title.a.text)

    #Plop the next kind of soup into the summary text bowel
    for paragraph in paragraphs_found:
        if(paragraph):
            if(paragraph.text):
                paragraphs.append(paragraph.text)

    #Picture scraping parameters
    url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Splinter Stuff
    browser.links.find_by_partial_text('FULL IMAGE').click()
    browser.links.find_by_partial_text('more info').click()
    browser.links.find_by_partial_text('1920 x 1200').click()

    #Fact Scraping parameters
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)

    #More Pictures.


    #Append it all
    Allspaceinfo = {
        "Headline" : headlines,
        "Teaser" : paragraphs,
        "Featured URL" :, #Whatever variable I end up making.
        "Hemisphere 1 URL":, #Same
        "Hemisphere 2 URL":, #Same
        "Hemisphere 3 URL":, #Same
        "Hemisphere 4 URL":, #Same
        "Table Data": tables
    }
    
   