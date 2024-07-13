import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.amazon.in/")
driver.maximize_window()
title =driver.title
print(title)
driver.find_element(By.ID,"nav-link-accountList").click()

# driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()

# driver.find_element(By.XPATH,"//a[normalize-space()='Try again']").click()

# Try again
time.sleep(10)
#driver.quit()