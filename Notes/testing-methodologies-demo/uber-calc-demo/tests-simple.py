import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

browser = webdriver.Chrome("chromedriver", options=chrome_options)

browser.get("http://localhost:5000")

assert browser.title == 'UberCalc'

x = browser.find_element(By.ID, 'x-field')
x.send_keys("3")
y = browser.find_element(By.ID, 'y-field')
y.send_keys("4")

btn = browser.find_element(By.ID, 'calc-button')
btn.click()

result = browser.find_element(By.ID, 'result')
assert result.text == "7"

browser.quit()
print('All tests were run.')