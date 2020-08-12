from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random
import sys

PATH = "F:\Program\Chrome(Driver)\chromedriver.exe"  
driver = webdriver.Chrome(PATH)

driver.get('https://www.netflix.com/id-en/')
print(driver.title)

search = driver.find_element_by_xpath('//*[@id="id_email_hero_fuji"]')
search.send_keys(sys.argv[1])
search.send_keys(Keys.RETURN)
sleep(5)
    # print(driver.page_source)
    # elem = driver.find_element_by_partial_link_text('Create Activity')
    # try:   
    #     if "Sign In" in driver.find_element_by_class_name('hybrid-login-form-main').text:
    #         print("KONTOL")
    #     else if "stepTitle" in driver.find_element_by_class_name('hybrid-login-form-main').text:

try:
        # elem =driver.find_element_by_class_name('hybrid-login-form-main').text
    if "Sign In" in driver.find_element_by_class_name('hybrid-login-form-main').text:
            print("KETEMU ANJING!")
            driver.quit()
except NoSuchElementException:
        driver.delete_all_cookies()
        driver.refresh()
        driver.quit()
        print("GA KETEMU")
        