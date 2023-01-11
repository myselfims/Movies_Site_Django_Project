from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless")  

browser = webdriver.Chrome(chrome_options=chrome_options)  
 
# browser = webdriver.Chrome()
'''
#-- FireFox
caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
browser = webdriver.Firefox(capabilities=caps)
'''
 
url = 'https://blog.officialboypalak.in/'
browser.get(url)
time.sleep(6) #seconds
inputElement = browser.find_element(By.PARTIAL_LINK_TEXT,'Start Verification')
inputElement.click()
 
# Give source code to BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'html.parser')
 
# Get JavaScript info from site
print(soup.find('title'))

time.sleep(5) #seconds
browser.close()