# import time

import unittest

from selenium import webdriver

# from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_access_user_view(self):
        self.browser.get('http://localhost:8000/')
        self.assertIn('RAPTR', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
