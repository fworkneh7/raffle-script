import csv
import time
from selenium import webdriver

chromepath = r"C:\Users\frazer\Desktop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromepath)
path = r"C:\Users\frazer\Documents\rafflescript\script_sheet.csv"

with open(path) as script_sheet:
    reader = csv.DictReader(script_sheet)
    for row in reader:
        driver.get("https://row.oneblockdown.it/collections/latest/products/air-force-1-low-cactus-jack")
        time.sleep(10)
        driver.find_element_by_id("product-form-4347800092743").click()
        #driver.find_element_by_class("action_button add_to_cart raffle-button").click()
