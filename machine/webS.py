"""in this project we are going to test the web scraping
using the beautifulsoup, pandas and urllib.request libraries
if you dont have this libraries installed please install them 
open you anaconda environment and lets start"""
#web scraping is an automated method used to extract large amount of data from websites.
#first find the URL you what to scrape
#next thing inspect the page you are going to scrape

#you can also use selenium if thats the library you prefer
#from selenium import webdriver
import bs4
from urllib.request import urlopen as url_open
from bs4 import BeautifulSoup as soup
import pandas as pds

#were to store the data collecte
all_product =[]
prices =[]
ratings =[]

my_url = 'https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2'

#this code will call urllib which will open up a 
# connection that will grabe the web page 
my_client = url_open(my_url)
page_web_html = my_client.read()
my_client.close()

#html parser
soup_page = soup(page_web_html, "html.parser")

#to check if it works use print statement
#print(soup_page.h1)

#find the class id you'll use
container = soup_page.findAll('a', href=True, attrs={'class':'_31qSD5'})

#pull the data you want to use
for contain in container:
    name = contain.find('div', attrs = {'class':'_3wU53n'})
    price = contain.find('div', attrs = {'class':'_1vC4OE _2rQ-NK'})
    rating = contain.find('div', attrs= {'class':'niH0FQ'})
    #for rate in rating:
     #   clean_rate = rate.find('span', )   
    #check if the loop works
    #print("name: ",  name)

    all_product.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

#save the file in a required format
    dataf = pds.DataFrame({'ProductsName':all_product,'Price':prices,'Rating_and_reveiws ':ratings})
    dataf.to_csv('text_product.csv', index=False, encoding='utf-8')

