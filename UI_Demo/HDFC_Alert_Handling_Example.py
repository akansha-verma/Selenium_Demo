import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.IE import IEDriverManager
# Step 1> Open Firefox
browser=webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2> Enter the URL
browser.get("https://netbanking.hdfcbank.com/netbanking/")
browser.switch_to.frame("login_page")
browser.find_element_by_xpath("//img[@alt='continue']").click()
alert_ele=browser.switch_to.alert
time.sleep((2))
alert_text=alert_ele.text
assert alert_text=="Customer ID  cannot be left blank."
alert_ele.accept()
time.sleep((15))
browser.quit()

https://opensource-demo.orangehrmlive.com/index.php/auth/login