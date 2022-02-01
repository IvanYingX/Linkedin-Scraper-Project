import sys
sys.path.append('Linkedin-Scraper-Project')
from scraper.methods import WebDriver
from scraper.secrets import (LINKEDINUSERNAME, LINKEDINPASSWORD)
import unittest
from selenium.webdriver.chrome.options import Options
from time import sleep

class WebDriverTestCase(unittest.TestCase):
    '''Test Class for testing WebDriver class from main script'''
    def setUp(self):
        '''Setting up an instance of the webdriver class for testing'''
        self.username = LINKEDINUSERNAME
        self.password = LINKEDINPASSWORD
        self.website = "https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&trk=login_reg_redirect"
        chrome_options = Options()
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        chrome_options.add_argument('--window-size=1920,1080')
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument(f'user-agent={user_agent}')
        self.instance = WebDriver(chrome_options, self.website, self.username, self.password)
        self.instance.driver.get(self.website)

    def test_get_current_url(self):
        expected_result = "https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&trk=login_reg_redirect"
        actual_result = self.instance.get_current_url()
        self.assertEqual(expected_result, actual_result)

    def test_accept_cookies(self):
        sleep(5)
        self.instance.accept_cookies()

    def test_log_me_in(self):
        sleep(5)
        self.instance.accept_cookies()
        sleep(5)
        self.instance.log_me_in()
        expected_result = "https://www.linkedin.com/feed/"
        actual_result = self.instance.driver.current_url
        self.assertEqual(expected_result, actual_result)
    
    def test_search_term(self):
        sleep(2)
        self.instance.accept_cookies()
        sleep(2)
        self.instance.log_me_in()
        sleep(2)
        self.instance.search_term('Data Science', 'England, United Kingdom')
        sleep(2)
        expected_result = "https://www.linkedin.com/jobs/search/?geoId=102299470&keywords=Data%20Science&location=England%2C%20United%20Kingdom"
        actual_result = self.instance.driver.current_url
        self.assertEqual(expected_result, actual_result)
    
    def tearDown(self):
        sleep(5)
        self.instance.driver.quit()


unittest.main(argv=[''], verbosity=2, exit=False)
