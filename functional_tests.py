from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#cap = DesiredCapabilities().FIREFOX
#cap['marionette'] = False

binary = FirefoxBinary(r'C:\Users\w23209\AppData\Local\Mozilla Firefox\firefox.exe')


browser = webdriver.Firefox(firefox_binary=binary)
browser.get('localhost:8000/')

assert 'Django' in browser.title