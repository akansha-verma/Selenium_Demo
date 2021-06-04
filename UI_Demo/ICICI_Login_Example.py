import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.IE import IEDriverManager
''' steps'''
# Step 1> Open Firefox
browser=webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2> Enter the URL
browser.get("https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=ICI&ITM=nli_personalb_personal_login_btn&_ga=2.178804460.973838477.1622284258-291133850.1622284258&_gl=1*39elos*_ga*MjkxMTMzODUwLjE2MjIyODQyNTg.*_ga_SKB78GHTFV*MTYyMjI4NDI2Mi4xLjAuMTYyMjI4NDI4MC40Mg..")
browser.switch_to.frame(0)
browser.find_element_by_name("").send_keys("1000")
time.sleep(5)
browser.find_element_by_link_text("Know More").click()
time.sleep(5)
# Step 3> Search & Enter the username and password field
browser.switch_to.default_content()
browser.switch_to.frame(1)
browser.find_element_by_link_text("Terms and Conditions").click()

#browser.quit()