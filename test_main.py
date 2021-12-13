from main import WebDriver
import unittest
from selenium.webdriver.chrome.options import Options


class WebDriverTestCase(unittest.TestCase):
    # Initialise scenario for test
    def setUp(self):
        username = "AiCoreOct2021@outlook.com"
        password = "Password123,,"
        self.website = "https://www.linkedin.com/feed/"
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.instance = WebDriver(chrome_options, self.website, username, password)

    def test_get_current_url(self):
        expected_result = "https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&trk=login_reg_redirect"
        self.instance.driver.get(self.website)
        actual_value = self.instance.get_current_url()
        self.assertEqual(expected_result, actual_value)

    def tearDown(self):
        del self.instance


unittest.main(argv=[''], verbosity=2, exit=False)
