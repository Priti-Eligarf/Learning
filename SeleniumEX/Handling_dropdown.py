import time
from selenium.webdriver.support import expected_conditions as ec

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# driver.get("https://www.echoecho.com/htmlforms11.htm")
driver.get("https://www.wikipedia.org/")

driver.maximize_window()
title = driver.title
print(title)
wait = WebDriverWait(driver, 10)

# driver.find_element(By.NAME, "dropdownmenu").send_keys("Cheese")
dropdown = driver.find_element(By.ID, "searchLanguage")
select = Select(dropdown)
select.select_by_visible_text("Eesti")
select.select_by_value("hi")

options = driver.find_elements(By.TAG_NAME, "option")

for option in options:
    print("options text is ", option.text, "lan attribute is " + option.get_attribute("lang"))
print("Total options are : ", len(options))

print("-----------------Find element by tag-----------------------")

links = driver.find_elements(By.TAG_NAME, "a")
print("Total Links are ", len(links))
for link in links:
    print("Link is", link.text, "------URL is: "+link.get_attribute("href"))

# print("--------ALL LINKS --------------------------------")
#
# block = driver.find_element(By.XPATH, "//nav[@aria-label='Other projects']")
# links = block.find_elements(By.TAG_NAME, "a")
#
# print("print 1st link : ", block.find_elements(By.TAG_NAME, "a").__getitem__(0).text)
# block.find_elements(By.TAG_NAME, "a").__getitem__(2)
# time.sleep(3)
# print("Total Links are ", len(links))
# for link in links:
#     print("Link is", link.text, "------URL is: " + lnk.get_attribute("href"))

# time.sleep(10)


print("--------ALL LINKS on the page--------------------------------")
lnk = driver.find_elements(By.TAG_NAME, "a");
print(len(lnk))

for lk in lnk:
    print("Link text is : ", lk.text, " .....Url is : " +lk.get_attribute("href"))
