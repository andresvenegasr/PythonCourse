from requests_html import HTMLSession, AsyncHTMLSession
from selenium import webdriver

url = "https://www.gandhi.com.mx/aprendendo-a-programar"

session = HTMLSession()
# r = session.get(url)

# price = r.html.find(".current-price")

# print(r.content)
# print(price)

driver = webdriver.Firefox()
driver.get(url)

driver.find_element_by_class_name("btn-cart").click()
