import time
from selenium.common.exceptions import TimeoutException
from Test_Scripts import XLUtil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Launch Browser
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2) Navigate to OrangeHRM
browser.get("https://opensource-demo.orangehrmlive.com/")
path = "OrangeHRM_TestData.xlsx"
rows = XLUtil.getRowCount(path, 'SignIn')
for r in range(2,rows+1):
    username_value = XLUtil.readData(path,'SignIn',r,1)
    password_value = XLUtil.readData(path,'SignIn',r,2)
    # Step 3) Enter UserName and Password
    username = browser.find_element_by_name("txtUsername")
    password = browser.find_element_by_name("txtPassword")
    submit = browser.find_element_by_name("Submit")
    username.send_keys(username_value)
    password.send_keys(password_value)
    # Step 4) Click Login
    submit.click()
    try:
        if browser.find_element_by_link_text("Dashboard").is_displayed():
            print("test is successful")
            Act_Res = browser.find_element_by_link_text("Dashboard").text
            XLUtil.writeData(path,'SignIn',r,3,"Test Successful")
            XLUtil.writeData(path, 'SignIn', r, 4, Act_Res)
            time.sleep(4)
            browser.find_element_by_id('welcome').click()
            time.sleep(2)
            browser.find_element_by_link_text('Logout').click()
    except:
    #else:
        print("test is un-successful")
        Act_msg = browser.find_element_by_id("spanMessage").text
        XLUtil.writeData(path, 'SignIn', r, 3,"Test Un-Successful")
        XLUtil.writeData(path, 'SignIn', r, 4, Act_msg)
browser.quit()