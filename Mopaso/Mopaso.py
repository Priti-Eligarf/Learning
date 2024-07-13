import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service("C:\ Users\Priti.Lale\drivers\Chrome\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://test.mopaso.momento.reisen/#/sign-in")

# Login with Admin
time.sleep(5)
#logo="/assets/images/logo-login.png"
# logofix = \

driver.find_element(By.CSS_SELECTOR, "img[src=/assets/images/logo-login.png]")
Act_title = driver.title
exp_title = "MoPaSo"
print(driver.title)


driver.find_element(By.CSS_SELECTOR, "input[placeholder=Username]").send_keys("Steffen")
driver.find_element(By.CSS_SELECTOR, "input[placeholder=Passwort]").send_keys("M0.P@so@2019")
driver.find_element(By.CSS_SELECTOR, "span.ui-button-text").click()
time.sleep(5)
