import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service("C:\ Users\Priti.Lale\drivers\Chrome\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://qa.wegive.tech")
# driver.find_element(By.Name"username" "Admin")
# driver.find_element("password" "password")
driver.maximize_window()
driver.implicitly_wait(5)
# driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div[2]/button").click()
driver.find_element(By.CSS_SELECTOR, "button.sc-fzqBkg[data-cy=next]").click()
# driver.find_element(By.LINK_TEXT, "Next").click()
print("load ")
# time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "button.sc-fzqBkg").click()
# time.sleep(10)
# driver.implicitly_wait(1000)
# driver.quit()
# /html/body/div/div[1]/div/div[2]/div[2]/button

# //*[@id="__next"]/div[1]/div/div[2]/div[2]/button
