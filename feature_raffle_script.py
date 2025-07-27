
import csv
import time
from selenium import webdriver


chromepath = r"C:\Users\frazer\Desktop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromepath)
path = r"C:\Users\frazer\Documents\rafflescript\script_sheet.csv"

with open(path) as script_sheet:
    reader = csv.DictReader(script_sheet)
    for row in reader:
        driver.get("https://feature.com/products/nike-air-fear-of-god-1-orange-pulse-raffle")
        driver.find_element_by_xpath("//*[@id='featArea']/div/div/a").click()
        driver.find_element_by_id("CustomerEmail").send_keys(row['email'] + '@gmail.com')
        driver.find_element_by_xpath("//*[@id='customer_login']/button").click()
        driver.find_element_by_xpath("//*[@id='swatch-1-9']").click()
        #time.sleep(3)
        #driver.send_keys( "\t" + "\t" + "\t" + " ")
