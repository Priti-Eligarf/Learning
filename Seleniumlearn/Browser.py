import time
from selenium import webdriver
from selenium.webdriver.common.by import By

'''driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
#driver = webdriver.Edge()  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')
t=driver.title
print(t)
assert "Google" in t
time.sleep(5) # Let the user actually see something!
#search_box = driver.find_element_by_id("input")
search_box=driver.find_element()
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)  # Let the user actually see something!'''
#driver.quit()'''
from selenium import webdriver

# Initialize the Chrome webdriver
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

# Open Google's homepage
driver.get('http://www.google.com/')

# Get the title of the page
title = driver.title
print("Page title:", title)

# Verify if "Google" is present in the title
assert "Google" in title, "Google is not present in the title."

# Locate the search box element by its name attribute
search_box=driver.find_element(By.NAME,'q')

# Type "ChromeDriver" into the search box
search_box.send_keys('ChromeDriver')
time.sleep(5)
driver.find_element(By.XPATH,'//@type="submit"').click()
time.sleep(20)
# Submit the search form
#search_box.submit()# Wait for a few seconds to let the user see the result
# time.sleep(5)  # Not necessary for this specific code

# Close the browser window
# driver.quit()  # Uncomment this line if you want to close the browser window
