import time
from selenium.webdriver.support import expected_conditions as ec

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
title = driver.title
# implicit Wiat
# driver.implicitly_wait(10)
print(title)
driver.find_element(By.ID, "nav-link-accountList").click()

driver.find_element(By.NAME, "email").send_keys('8308949781')
driver.find_element(By.ID, "continue").click()
"""
# Explicit Wait
# element = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, "ap_password")))
# element.send_keys('Rajyog@2024')
"""
WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, "ap_password")))
driver.find_element(By.ID, "ap_password").send_keys('Rajyog@2024')
driver.find_element(By.ID, "auth-signin-button").click()
# driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()

# driver.find_element(By.XPATH,"//a[normalize-space()='Try again']").click()

# Try again
time.sleep(10)
# driver.quit()
