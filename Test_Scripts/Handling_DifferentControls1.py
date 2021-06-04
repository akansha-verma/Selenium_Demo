import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.select import Select

# Step 1) Open Firefox
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()

# Step 2) Navigate to OrangeHRM
browser.get("https://www.testandquiz.com/selenium/testing.html")
username = browser.find_element_by_xpath("//b[normalize-space()='This is sample text.']").text
assert username == 'This is sample text.'
print(username)
#winHandleBefore = browser.current_window_handle
#browser.find_element_by_link_text("This is a link").click()
#browser.switch_to.window(winHandleBefore);
browser.find_element_by_id("fname").send_keys("Automation Test")
browser.find_element_by_id("idOfButton").click()
browser.find_element_by_id("male").click()
browser.find_element_by_class_name("Automation").click()
select = Select(browser.find_element_by_id('testingDropdown'))
selected_option = select.first_selected_option
ab = selected_option.text
ac = browser.find_element_by_id("dblClkBtn")
actions = ActionChains(browser)
actions.double_click(ac)
# perform the operation on the element
actions.perform()
time.sleep(5)
#Close the browser
browser.quit()