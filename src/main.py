from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

item = input(str('Searching Item = '))

browser = webdriver.Chrome()
browser.get('https://feature.com/')
browser.implicitly_wait(5) # normaly, this bot will try the function every 0.5s, maxnium time is the number you put

searchBar = browser.find_element_by_id('acp_magento_search_id')
searchBar.send_keys('{0}\n'.format(item))

sleep(10)
browser.close()