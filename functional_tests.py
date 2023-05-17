
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By




class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_login_page_and_register_page_hyperlink(self):
        # User has heard about a cool new online to-do app. He goes to check out its homepage
        self.browser.get('http://127.0.0.1:8000')

        # He notices the login page with register option
        self.assertIn('Login Page', self.browser.title)
        p_text = self.browser.find_element(By.TAG_NAME, "p").text
        self.assertIn('Want To Register Account?', p_text)

        # He clicks on "i want to register" button and gets redirected to register page


        # He fill out the register form and clicks register button
        self.fail('Finish the test!')
        # He gets redirected to login page with message saying that he registered that account

if __name__ == '__main__':
    unittest.main()
