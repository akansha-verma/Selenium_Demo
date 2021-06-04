import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class SearchText(unittest.TestCase):
    def setUp(self):
        #Create a new chrome session
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        #Target URL
        self.driver.get("https://www.google.com/")
    def test_search_by_text(self):
        self.search_field=self.driver.find_element_by_name("q")
        #enter search keywords and submit
        self.search_field.send_keys("Interview Questions on Selenium")
        self.search_field.submit()
        # Get the list of elements which are displayed after the search
        lists=self.driver.find_element_by_name("btnK").click()
        no=len(lists)
        print(no)
        self.assertEqual(15,no)

    def tearDown(self):
        self.driver.quit()

    if __name__=='__main__':
        unittest.main()