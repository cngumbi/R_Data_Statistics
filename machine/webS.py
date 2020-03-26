"""in this project we are going to test the web scraping
using the beautifulsoup libraries and selenium
if you dont have this libraries installed please install them 
open you anaconda environment and lets start"""
#web scraping is an automated method used to extract large amount of data from websites.
#first find the URL you what to scrape
#next thing inspect the page you are going to scrape

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pds

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products = [] #list to store name of product
prices = [] #list to store price of the product
ratings = [] #list to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")


