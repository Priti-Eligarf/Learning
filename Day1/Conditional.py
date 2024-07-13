'''import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\ Users\Priti.Lale\drivers\Chrome\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://test.mopaso.momento.reisen/#/sign-in")
driver.maximize_window()'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0, 600);")
