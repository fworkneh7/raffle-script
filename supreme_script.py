import csv
import time
from selenium import webdriver


chromepath = r"C:\Users\frazer\Desktop\chromedriver.exe"
driver = webdriver.Chrome(chromepath)
path = r"C:\Users\frazer\Documents\rafflescript\script_sheet.csv"

#open gmail page
driver.get("https://gmail.com")

#enter username
email_signin = driver.find_element_by_id("identifierId")
email_signin.send_keys("esahlemariam85@gmail.com")

#go to password page
driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
time.sleep(1)

#eter password
password_sumbit = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
password_sumbit.send_keys("iluvfrazer")
time.sleep(1)

#press submit for login
driver.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
time.sleep(1)

with open(path) as script_sheet:
    reader = csv.DictReader(script_sheet)
    for row in reader:
        product = driver.get("https://www.supremenewyork.com/shop/all/jackets")
        product_select = product.send_keys("\t" * 18)
        product_select.click()
        driver.find_element_by_id("s").send_keys("Medium")
        driver.find_element_by_xpath("//*[@id='cart-add']/fieldset[1]").click()
