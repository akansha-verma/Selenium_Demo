from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import unittest

class Draganddrop():
    def dd(self):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://jqueryui.com/resources/demos/droppable/default.html")

        action = ActionChains(browser)

        drag = browser.find_element_by_id("draggable")
        drop = browser.find_element_by_id("droppable")

        action.drag_and_drop(drag,drop).perform()

        browser.close()

if __name__ == '__main__':
    unittest.main()