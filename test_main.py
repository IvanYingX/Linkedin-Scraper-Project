from main import WebDriver
import unittest
from selenium.webdriver.chrome.options import Options

class WebDriverTestCase(unittest.TestCase):
    # Initialise scenario for test
    def setUp(self):
        username = "AiCoreOct2021@outlook.com"
        password = "Password123,,"
        website = "https://www.linkedin.com/feed/"
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.instance = WebDriver(address=website,username=username,password=password)

    def test_get_current_url(self):
        expected_result = "https://www.linkedin.com/feed/"
        actual_value = self.instance.get_current_url()
        self.assertEqual(expected_result,actual_value)

    def tearDown(self):
        del self.instance