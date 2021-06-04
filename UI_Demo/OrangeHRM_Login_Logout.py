import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.IE import IEDriverManager
# Step 1> Open Firefox
browser=webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2> Enter the URL
browser.get("https://opensource-demo.orangehrmlive.com/")
# Step 3> Search & Enter the username and password field
browser.find_element_by_name("txtUsername").send_keys("Admin")
browser.find_element_by_name("txtPassword").send_keys("admin123")
browser.find_element_by_name("Submit").click()
wait=WebDriverWait(browser,20)
page_title=browser.title
print(page_title)
assert page_title=="OrangeHRM"
# Logout checking
browser.find_element_by_link_text("Dashboard").is_displayed()
browser.find_element_by_partial_link_text("Welcome").click()
time.sleep(1)
browser.maximize_window()
browser.find_element_by_link_text("Logout").click()
browser.find_element_by_id("logInPanelHeading").is_displayed()
# Close the Browser
browser.close()