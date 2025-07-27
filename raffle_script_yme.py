import csv
import time
from selenium import webdriver

chromepath = r"C:\Users\frazer\Desktop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromepath)
driver1 = webdriver.Chrome(chromepath)

path = r"C:\Users\frazer\Documents\rafflescript\script_sheet.csv"

with open(path) as script_sheet:
    reader = csv.DictReader(script_sheet)
    for row in reader:
        driver.get("https://row.oneblockdown.it/collections/latest/products/air-force-1-low-cactus-jack")
        driver.find_element_by_class("action_button add_to_cart raffle-button").click()
        driver.find_element_by_id("inputName").send_keys("Frazer")
        driver.find_element_by_id("inputEmail").send_keys(row['email'] + '@bakershill.club')
        driver.find_element_by_id("inputCity").send_keys("Silver Spring")
        driver.find_element_by_id("inputState").send_keys("MD")
        driver.find_element_by_id("inputZip").send_keys("20906")
        driver.find_element_by_id("inputPhone").send_keys(row['phone'])
        driver.find_element_by_id("inputShoeSize").send_keys("9")
        time.sleep(10)

    # open gmail page
    # driver.get("https://gmail.com")

    # enter username
    # email_signin = driver.find_element_by_id("identifierId")
    # email_signin.send_keys("esahlemariam85@gmail.com")


    # go to password page
    # driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
    # time.sleep(2)

    # enter password
    # password_sumbit = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
    # password_sumbit.send_keys("iluvfrazer")
    # time.sleep(2)

    # press submit for login
    # driver.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
    # time.sleep(5)
