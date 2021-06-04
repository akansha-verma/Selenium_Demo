import time
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

browser=webdriver.Chrome(executable_path=ChromeDriverManager().install())

browser.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

browser.find_element_by_xpath("//button[normalize-space()='Click for JS Alert']").click()
alert=Alert(browser)
print(alert.text)
alert.accept()

actual_text=browser.find_element_by_xpath("//p[@id='result']")
print(actual_text.text)
assert actual_text.text=="You successfully clicked an alert"
