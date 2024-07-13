from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options for incognito mode
#chrome_options = Options()
#chrome_options.add_argument("--incognito")

# Initialize the Chrome webdriver with the configured options
driver = webdriver.Edge()
# Open the Gmail login page
driver.get('https://www.linkedin.com/login')

# Find the email input field and enter your email address
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys("varsha.g1800@gmail.com")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("Rajyog@2013")

next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")
next_button.click()

driver.quit()
