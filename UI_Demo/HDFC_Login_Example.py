import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.IE import IEDriverManager
''' steps'''
# Step 1> Open Firefox
browser=webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2> Enter the URL
browser.get("https://netbanking.hdfcbank.com/netbanking/")
browser.switch_to.frame(0)
browser.find_element_by_name("fldLoginUserId").send_keys("1000")
time.sleep(5)
browser.find_element_by_link_text("Know More").click()
time.sleep(5)
# Step 3> Search & Enter the username and password field
browser.switch_to.default_content()
browser.switch_to.frame(1)
browser.find_element_by_link_text("Terms and Conditions").click()

#browser.quit()