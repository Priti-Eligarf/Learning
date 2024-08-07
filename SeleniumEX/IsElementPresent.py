import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


# def is_element_present(id):
#     try:
#         driver.find_element_by_id(id)
#         return True
#     except NoSuchElementException:
#         return False

# def is_element_present(how, what):
#     try:
#         driver.find_element(by=how, value=what)
#         return True
#     except NoSuchElementException:
#         return False

def is_element_present(how, what):
    if len(driver.find_elements(by=how, value=what)) == 0:
        return False
    else:
        return True


driver = webdriver.Chrome()

driver.get("https://www.gmail.com/")
driver.maximize_window()
driver.implicitly_wait(1)
# print(driver.find_element(By.ID, "identifireId221313").is_displayed())
# print(is_element_present("identifireId"))
print(is_element_present(By.ID, "identifierId"))
print(is_element_present(By.XPATH, "//input[@id='identifierId23']"))
