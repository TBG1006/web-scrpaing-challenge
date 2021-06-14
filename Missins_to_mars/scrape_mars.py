import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
import os
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect

def scrape_news():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Scrape title and teaser for latest news
    news_url = "https://redplanetscience.com/#"
    browser.visit(news_url)
    news_html=browser.html
    news_soup=BeautifulSoup(news_html,'html.parser')
    article_title = news_soup.find("div", class_="content_title")
    article_teaser = news_soup.find("div", class_="article_teaser_body")

    #close browser
    browser.quit()

    return (article_title,article_teaser)

def scrape_featured_image():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Go to image landing page
    image_url ="https://spaceimages-mars.com/"
    browser.visit(image_url)

    # Click full image to get image url
    browser.links.find_by_partial_text('FULL IMAGE').click()    
    featured_image_url = https://spaceimages-mars.com/image/featured/mars1.jpg

    browser.quit()

    return featured_image_url

def scrape_hem():
    #extract html
    hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(hemispheres_url)

    hem_html = browser.html
    hem_soup = BeautifulSoup(hem_html, "html.parser")
    hem_results = hem_soup.find("div", class_="result-list")

    cerb_image = hem_results.find_all('img')[0]["src"]
    cerb_path = hemispheres_url + cerb_image
    cerb_title = hem_results.find_all('img')[0]["alt"]

    schiap_image = hem_results.find_all('img')[1]["src"]
    schiap_path = hemispheres_url + schiap_image
    schiap_title = hem_results.find_all('img')[1]["alt"]

    syrtis_image = hem_results.find_all('img')[2]["src"]
    syrtis_path = hemispheres_url + syrtis_image
    syrtis_title = hem_results.find_all('img')[2]["alt"]

    valles_image = hem_results.find_all('img')[2]["src"]
    valles_path = hemispheres_url + valles_image
    valles_title = hem_results.find_all('img')[2]["alt"]

    hem_urls = [
    {"title": cerb_title, "img_url": cerb_path},
    {"title": schiap_title, "img_url": schiap_path},
    {"title": syrtis_title, "img_url": syrtis_path},
    {"title": valles_title, "img_url": valles_path},
    ]
    
    browser.quit()

    return hem_urls

def scrape_final():
    article_title,article_teaser = scrape_news()
    featured_image_url = scrape_featured_image()
    hem_urls = scrape_hem()

    data = {
        "Most Recent News":article_title,
        "Description":article_teaser,
        "Featured Image":featured_image_url,
        "Hemispheres":featured_image_url,
    }

    return data