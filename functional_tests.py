
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User has heard about a cool new online to-do app. He goes to check out its homepage
        self.browser.get('http://127.0.0.1:8000')

        # He notices the login page with register option
        self.fail('Finish the test!')

        # He clicks on "i want to register" button and gets redirected to register page

        # He fill out the register form and clicks register button

        # He gets redirected to login page with message saying that he registered that account

if __name__ == '__main__':
    unittest.main()
