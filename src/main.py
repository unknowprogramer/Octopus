from selenium import webdriver
import re

def feature(link):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(10)

    addToCart = browser.find_element_by_name('Add to Cart')
    addToCart.click()

link = input(str('Website Link = '))
if re.search('feature', link):
    feature(link)