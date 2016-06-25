from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://bayo.pythonanywhere.com')

assert 'Django' in browser.title
