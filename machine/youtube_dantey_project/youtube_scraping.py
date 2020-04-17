"""in this project we are going to test the web scraping
using the beautifulsoup, pandas and urllib.request libraries
if you dont have this libraries installed please install them 
open you anaconda environment and lets start"""
#web scraping is an automated method used to extract large amount of data from websites.
#first find the URL you what to scrape
#next thing inspect the page you are going to scrape

#from selenium import webdriver
import bs4
from bs4 import BeautifulSoup as soup
import pandas as pds
import requests
import smtplib
import time


my_url = 'https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2'

#you can create a header 
headers = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}

prices =[]

def webScrap():
    #this code will grabe the website
    html_page = requests.get(my_url, headers=headers)

    #html parser
    soup_page = soup(html_page.content, "html.parser")

    #find the class id you'll use
    container_trend = soup_page.findAll('a', href=True, attrs={'class':'_31qSD'})

    #check the length of the container
    for contain in container_trend:
        price = contain.find('div', attrs = {'class':'_1vC4OE _2rQ-NK'})

        #prices.append(price.text)
        #check if the data is present on the 
        convert_price = price
    #if (convert_price < 60):
    #    send_mail()

        print(convert_price)

#create a function to send an email 
"""def send_mail():
    #create the function form this point
    #create a connection with google
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls() #to encrypt the massage
    server.ehlo()

    #login to the email
    server.login('cngumb35@gmail.com','0720543605')

    #create the email
    subject = 'the views have increased'
    body = 'check the youtube link: add the link'

    #format the message
    msg = f"Subject: {subject} \n\n {body}"

    #send the email
    server.sendmail(
        'cngumbi35@gmail.com',
        'afrjon36@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()

while(True):
    webScrap()
    time.sleep(60 * 60 * 24)
    """
webScrap()