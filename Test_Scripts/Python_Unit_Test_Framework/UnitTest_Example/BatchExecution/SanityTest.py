import unittest
# get all tests from SearchText and HomePageTest class
from Test_Scripts.UnitTest_Example.UnitTest_Decorator.Draganddrop import Draganddrop
from Test_Scripts.UnitTest_Example.UnitTest_Decorator.UnitTest_Setup_TearDown import SearchText
from Test_Scripts.UnitTest_Example.UnitTest_Assertions import Assertions_assertIs_OrangeHRM

drag_drop = unittest.TestLoader().loadTestsFromName(Draganddrop.dd(Draganddrop))
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromModule(Assertions_assertIs_OrangeHRM)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text, drag_drop])

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(title='Test Summary Report', description='Execution of Smoke Tests', report_name='Smoke Test Report')

# run the suite using runner object, with customized details.
runner.run(test_suite)
# run the suite using HTMLTestRunner, which will have default file name
# report name with date and time
#HTMLTestRunner.HTMLTestRunner(verbosity=2).run(test_suite)
