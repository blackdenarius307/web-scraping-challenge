#Importations
import splinter
import pandas as pd
import time
from splinter import Browser
from bs4 import BeautifulSoup

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
    #Sleep
    time.sleep(5)
    
    #Featured picture scraping parameters
    url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    #Click Through Stuff
    browser.links.find_by_partial_text('FULL IMAGE').click()
    browser.links.find_by_partial_text('more info').click()

    #Set the soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Grab the Image
    text_soup = soup.find_all("figure", class_="lede")
    figure = text_soup[0]
    image_soup = figure.find_all("a", href = True)
    URL_bit = image_soup[0]["href"]
    Full_URL = f'https://www.jpl.nasa.gov{URL_bit}'

    #Sleep
    time.sleep(5)
    
    #Fact Scraping parameters
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    Mars_facts_DF = tables[0]
    
    #Sleep
    time.sleep(5)

    #Initial Hemisphere List
    Hemisphere_pics = []

    #Hemisphere 1 
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    #Browser work
    browser.visit(url)
    browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()
    #Prepare the Soup for Hemisphere 1
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    text_soup = soup.find_all("div", class_="downloads")
    figure = text_soup[0]
    image_soup = figure.find_all("a", href = True)
    URL_bit = image_soup[0]["href"]
    Hemisphere_1_dict = {"title": "Cerberus Hemisphere", "img_url": URL_bit}
    Hemisphere_1_copy = Hemisphere_1_dict.copy()
    Hemisphere_pics.append(Hemisphere_1_copy)

    #Sleep
    time.sleep(5)

    #Hemisphere 2 
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    #Browser work
    browser.visit(url)
    browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()
    #Prepare the Soup for Hemisphere 2
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    text_soup = soup.find_all("div", class_="downloads")
    figure = text_soup[0]
    image_soup = figure.find_all("a", href = True)
    URL_bit = image_soup[0]["href"]
    Hemisphere_2_dict = {"title": "Schiaparelli Hemisphere", "img_url": URL_bit}
    Hemisphere_2_copy = Hemisphere_2_dict.copy()
    Hemisphere_pics.append(Hemisphere_2_copy)

    #Sleep
    time.sleep(5)

    #Hemisphere 3 
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    #Browser work
    browser.visit(url)
    browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()
    #Prepare the Soup for Hemisphere 3
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    text_soup = soup.find_all("div", class_="downloads")
    figure = text_soup[0]
    image_soup = figure.find_all("a", href = True)
    URL_bit = image_soup[0]["href"]
    Hemisphere_3_dict = {"title": "Syrtis Major Hemisphere", "img_url": URL_bit}
    Hemisphere_3_copy = Hemisphere_3_dict.copy()
    Hemisphere_pics.append(Hemisphere_3_copy)

    #Sleep
    time.sleep(5)

    #Hemisphere 4 
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    #Browser work
    browser.visit(url)
    browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()
    #Prepare the Soup for Hemisphere 4
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    text_soup = soup.find_all("div", class_="downloads")
    figure = text_soup[0]
    image_soup = figure.find_all("a", href = True)
    URL_bit = image_soup[0]["href"]
    Hemisphere_4_dict = {"title": "Valles Marineris Hemisphere", "img_url": URL_bit}
    Hemisphere_4_copy = Hemisphere_4_dict.copy()
    Hemisphere_pics.append(Hemisphere_4_copy)

    #Append it all
    Allspaceinfo = {
        "Headline" : headlines,
        "Teaser" : paragraphs,
        "Featured URL" : Full_URL,
        "Table Data": Mars_facts_DF,
        "Hemisphere Pics" : Hemisphere_pics
    }
    
    #Close Browser After Scraping
    browser.quit()

    #Return Results
    return Allspaceinfo
   