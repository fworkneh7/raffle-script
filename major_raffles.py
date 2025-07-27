import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromepath = r"C:\Users\frazer\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromepath)
path = r"C:\Users\frazer\OneDrive\Documents\Python Scripts\rafflescript\MAJOR RAFFLE SCRIPT\major.csv"

with open(path) as script_sheet:
    reader = csv.DictReader(script_sheet)
    driver.get("https://www.majordc.com/dunklowsp")
    rowh = 0
    for row in reader:
        driver.get("https://www.majordc.com/dunklowsp")
        driver.find_element_by_name("fname").send_keys(row['fn'])
        time.sleep(2)
        driver.find_element_by_name("lname").send_keys(row['ln'])
        time.sleep(2)
        driver.find_element_by_id("text-yui_3_17_2_1_1572627776493_23134-field").send_keys(row['email'] + '@bakershill.club')
        time.sleep(2)
        driver.find_element_by_id("select-yui_3_17_2_1_1572627776493_23833-field").send_keys(row['size'])
        time.sleep(2)
        driver.find_element_by_id("text-yui_3_17_2_1_1589922755655_19309-field").send_keys('20906')
        time.sleep(1)
        uname = driver.find_element_by_id("text-yui_3_17_2_1_1589922755655_19309-field")
        uname.send_keys(Keys.TAB, Keys.ENTER)
        time.sleep(10)
        driver.execute_script("window.open('https://www.majordc.com/dunklowsp');")
        rowh = rowh+1
        driver.switch_to_window(driver.window_handles[rowh])

        # driver.find_element_by_class("action_button add_to_cart raffle-button").click()
