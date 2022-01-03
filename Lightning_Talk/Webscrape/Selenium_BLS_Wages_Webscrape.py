#!/usr/bin/env python
# coding: utf-8

# We must first import the required libraries.

from selenium import webdriver
import os
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By


# Set our download directory as the current working directory.

cwd = os.getcwd()
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : cwd}
chrome_options.add_experimental_option('prefs', prefs)

try:
    # Configure and start the browser driver.

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 2)


    # Navigate to a starting url.

    url = "https://www.bls.gov/cps/"
    driver.get(url)


    # Click the "Earnings" link.

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/table/tbody/tr/td[1]/div/div[2]/ul/li[6]/a').click()
    wait


    # Click on "Most requested series" link.

    driver.find_element(By.XPATH, '//*[@id="bodytext"]/ul[1]/li[3]/ul/li[2]/a').click()
    wait


    # Check the boxes for median weekly earnings of full-time employees.

    driver.find_element(By.XPATH, '//*[@id="bodytext"]/form/dl/dd[1]/input').click()
    time.sleep(.3)
    driver.find_element(By.XPATH, '//*[@id="bodytext"]/form/dl/dd[2]/input').click()
    time.sleep(.3)
    driver.find_element(By.XPATH, '//*[@id="bodytext"]/form/dl/dd[3]/input').click()
    time.sleep(.3)


    # Click on "Retrieve data".

    driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/form/p/input[1]').click()
    wait


    # From the dropdown, select "1979" as our starting year
    # And check the box to include annual averages.

    year_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="from-year"]'))
    year_dropdown.select_by_visible_text('1979')
    time.sleep(.3)
    driver.find_element(By.ID, 'annualAveragesRequested').click()
    time.sleep(.3)


    # Click the "GO" button.

    driver.find_element(By.XPATH, '//*[@id="bodytext"]/div[1]/form/span[1]/span[2]/input').click()
    wait


    # Set a variable for all the Excel download buttons on the page.

    excel_links = driver.find_elements(By.XPATH, '//input[contains(@id, "download_xlsx")]')


    # And click each of them.

    for link in excel_links:
        link.click()
        time.sleep(2)


# Close the browser.
finally:
    driver.quit()

