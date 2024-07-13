import time

from selenium import webdriver

# driver = webdriver.Chrome()
driver =webdriver.Edge()
driver.get("http://www.google.com")
driver.maximize_window()
title =driver.title
print(title)
time.sleep(10)
driver.quit()

