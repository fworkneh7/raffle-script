import csv, time
from selenium import webdriver


chromepath = r"C:\Users\frazer\Desktop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromepath)
driver1 = webdriver.Chrome(chromepath)

path = r"C:\Users\frazer\Documents\rafflescript\script_sheet_ubiq.csv"

with open(path) as script_sheet:
    reader = csv.DictReader(script_sheet)
    driver.get("https://releases.ubiqlife.com/raffle/yeezy350black_nov29.html")
    rowh = 0
    for row in reader:
        driver.find_element_by_id("inputEmail").send_keys(row['email'] + '@bakershill.club')
        driver.find_element_by_id("inputFirst_Name").send_keys(row['fname'])
        driver.find_element_by_id("inputLast_Name").send_keys(row['lastn'])
        driver.find_element_by_id("inputCity").send_keys(row['city'])
        driver.find_element_by_id("inputState").send_keys("MD")
        driver.find_element_by_id("inputStore").send_keys("Ubiq Georgetown")
        driver.find_element_by_id("inputZip").send_keys("20906")
        driver.find_element_by_id("inputPhone").send_keys(row['phone'])
        driver.find_element_by_id("inputShoeSize").send_keys(row['size'])
        driver.find_element_by_id("inputBirthday").send_keys(row['bday'])
        driver.execute_script("window.open('https://releases.ubiqlife.com/raffle/yeezy350black_nov29.html');")
        rowh = rowh+1
        driver.switch_to_window(driver.window_handles[rowh])
