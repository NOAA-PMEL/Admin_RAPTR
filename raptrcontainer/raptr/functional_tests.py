from selenium import webdriver
import unittest

class NewVistiorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_access_user_view(self):
        self.browser.get('http://localhost:8000/')
        self.assertIn('RAPTR', self.browser.title)
#        self.fail('Load of RAPTR Dashboard Failed.')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
