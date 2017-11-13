import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Chrome('c:\chromedriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://demo.testerka.pl")

# driver title assertion
title = driver.title
print(title)
assert title == u'Demo Testerka.pl'

# Sign up
driver.find_element_by_class_name('login').click()
driver.find_element_by_id('email_create').send_keys("mail@mail.mail")
driver.find_element_by_id('SubmitCreate').click()
assert "YOUR PERSONAL INFORMATION" == driver.find_element_by_xpath('//*[@id="account-creation_form"]/div[1]/h3').text
driver.find_element_by_id('id_gender1').click()
driver.find_element_by_id('customer_firstname').send_keys("Test")
driver.find_element_by_id('customer_lastname').send_keys("User")
driver.find_element_by_id('passwd').send_keys("12345678")
driver.find_element_by_id('days').click()
driver.find_element_by_xpath('//*[@id="days"]/option[10]').click()
driver.find_element_by_id('months').click()
driver.find_element_by_xpath('//*[@id="months"]/option[4]').click()
driver.find_element_by_id('years').click()
driver.find_element_by_xpath('//*[@id="years"]/option[32]').click()
driver.find_element_by_id('newsletter').click()
driver.find_element_by_id('optin').click()

# close the window
driver.quit()