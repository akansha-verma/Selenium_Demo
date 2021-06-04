from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
''' steps'''
# Step 1> Open Firefox
browser=webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2> Enter the URL
browser.get("https://opensource-demo.orangehrmlive.com/")
# Step 3> Search & Enter the username and password field
browser.find_element_by_name("txtUsername").send_keys("Admin")
browser.find_element_by_name("txtPassword").send_keys("admin123")
browser.find_element_by_name("Submit").click()

#time.sleep(5)
# Step 4>
page_title=browser.title
print(page_title)
assert page_title=="OrangeHRM"
browser.quit()