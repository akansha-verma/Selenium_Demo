import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains
''' steps'''

# Step 1> Open Firefox
browser=webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2> Enter the URL
browser.get("https://www.yatra.com/")
browser.maximize_window()
action=ActionChains(browser)
parent_level_menu=browser.find_element_by_xpath("//a[contains(text(),'My Account')]")
action.move_to_element(parent_level_menu).perform()
browser.find_element_by_id("signInBtn").click()
page_title=browser.title
print(page_title)
assert page_title=="Yatra Account"
browser.find_element_by_id("login-input").send_keys("9871515666")
browser.find_element_by_id("login-continue-btn").click()
time.sleep(2)
browser.find_element_by_id("otp-input").send_keys("1")
time.sleep(12)
browser.find_element_by_id("verify-otp").click()
time.sleep(10)
browser.find_element_by_id("BE_flight_origin_city").send_keys("BOM")
time.sleep(3)
browser.quit()