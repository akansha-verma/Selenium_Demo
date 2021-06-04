from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.IE import IEDriverManager
from selenium.webdriver.chrome.options import Options
''' steps'''
opt= Options()
opt.set_headless(True)
opt.add_argument('incognito')
#opt.headless
# Step 1> Open Firefox
browser=webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=opt)
# Step 2> Enter the URL
browser.get("https://opensource-demo.orangehrmlive.com/")
# Step 3> Search & Enter the username and password field
username=browser.find_element_by_xpath("//input[@name='txtUsername']")
username.send_keys("Admin")
password=browser.find_element_by_xpath("//input[@name='txtPassword']")
password.send_keys("admin123")
submit=browser.find_element_by_xpath("//input[@name='Submit']")
submit.click()
#time.sleep(5)
# Step 4>
page_title=browser.title
print(page_title)
assert page_title=="OrangeHRM"
browser.quit()