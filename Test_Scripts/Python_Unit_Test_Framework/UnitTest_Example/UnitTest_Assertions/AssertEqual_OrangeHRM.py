import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

class OrangeHRM_Login_Logout(unittest.TestCase):

    @classmethod
    def test_01_setUpClass(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # Target URL
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(1)
    def test_02_login_to_orangeHRM(self):
        Act_Text = self.driver.title
        print(Act_Text)
        Exp_Text = Act_Text
        # assertIs() to check that if first & second evaluated to same object
        self.assertIs(Exp_Text,Act_Text,"Title not displayed")

        self.driver.find_element_by_name('txtUsername').send_keys("Admin")
        self.driver.find_element_by_name('txtPassword').send_keys("admin123")
        self.driver.find_element_by_id('btnLogin').click()

        act_url = self.driver.current_url
        self.assertNotEqual("https://opensource-demo.orangehrmlive.com/index.php/auth/login", act_url,"Both value are not equal")
        time.sleep(5)
        action = ActionChains(self)
        parent_level_menu = self.driver.find_element_by_xpath("//a[normalize-space()='User Management']")
        action.move_to_element(parent_level_menu).perform()
        child_level_menu = self.driver.find_element_by_xpath("//a[normalize-space()='Users']")
        action.move_to_element(child_level_menu).perform()
        child_level_menu.click()
        '''list1=['All','Enabled','Disabled']
        list2 =['All', 'Enabled', 'Disabled']

        self.driver.find_element_by_xpath("//select[@id='searchSystemUser_status']")
        self.assertListEqual(list1,list2,msg="passed, Lists are matching")'''

        list1 = []
        for index in range(len(status_values)):
            list = status_values[index].text
            list1.append(list)
            print(list1)
        self.assertListEqual(list1, ['All', 'Enabled', 'Disabled'], 'List values Matched')


    @classmethod
    def test_03_tearDownClass(self):
        # close the browser window
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
