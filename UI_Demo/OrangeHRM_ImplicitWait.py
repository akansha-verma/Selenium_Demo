from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.IE import IEDriverManager

''' steps'''

# Step 1> Open Firefox
#browser=webdriver.Edge(executable_path='C:\\Users\\admin\\Desktop\\Selenium_Python_Training\\msedgedriver.exe')
#browser=webdriver.Chrome("C://Users//admin//PycharmProjects//Selenium_Trainin//Browser_Driver\chromedriver.exe")
#browser=webdriver.Chrome()
#browser=webdriver.Firefox()
browser=webdriver.Chrome(executable_path=ChromeDriverManager().install())
#browser=webdriver.Firefox(executable_path=GeckoDriverManager().install())
#browser=webdriver.Ie(executable_path=IEDriverManager().install())
# Step 2> Enter the URL
browser.get("https://opensource-demo.orangehrmlive.com/")
# Step 3> Search & Enter the username and password field
browser.find_element_by_name("txtUsername").send_keys("Admin")
browser.find_element_by_name("txtPassword").send_keys("admin123")
browser.find_element_by_name("Submit").click()
browser.implicitly_wait(5)
#time.sleep(5)
# Step 4>
page_title=browser.title
print(page_title)
assert page_title=="OrangeHRM"
browser.quit()