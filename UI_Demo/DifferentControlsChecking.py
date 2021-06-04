from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.IE import IEDriverManager
''' steps'''
# Step 1> Open Firefox
browser=webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2> Enter the URL
browser.get("https://www.testandquiz.com/selenium/testing.html")
sample_text=browser.find_element_by_xpath("//b[normalize-space()='This is sample text.']").text
assert sample_text=="This is sample text."
print(sample_text)

browser.find_element_by_link_text("This is a link").click()
alert_ele=browser.switch_to.alert
alert_text=alert_ele.text
print("alert_text")
alert_text.accept()
print("Link Clicked")


#browser.find_element_by_id("fname")
'''browser.find_element_by_name("txtPassword").send_keys("admin123")
browser.find_element_by_name("Submit").click()
browser.implicitly_wait(5)
#time.sleep(5)
# Step 4>
page_title=browser.title
print(page_title)
assert page_title=="OrangeHRM"'''
browser.close()