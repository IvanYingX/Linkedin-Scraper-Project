from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class WebDriver():
    '''
    WebDriver class used to move through a website and find elements inside

    Attributes:
        address (str): The address of the website that will be scraped'''

    def __init__(self, chrome_options, address: str, username: str, password: str):
        # ChromeDriverManager installs webdriver into cache automatically
        self.address = address
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def search_term():
        # TODO: create function that searches for a term in the websites search
        # bar and clicks "see all job results button"
        pass

    def collect_job_list():
        # TODO: create function that looks for element that contains the
        # list of job postings on the current page
        pass

    def find_next_page():
        # TODO: create function that finds next page element
        pass

    def previous_page():
        # TODO: create function that finds the previous page element
        pass

    def get_current_url(self):
        '''
        Function that returns current URL of webdriver
        '''
        return self.driver.current_url

    def accept_cookies(self):
        '''
        Function that finds manage cookies and accept cookies buttons by
        class name and then clicks the accept cookies button
        '''
        both_buttons = self.driver.find_elements_by_class_name("artdeco-global-alert-action.artdeco-button.artdeco-button--inverse.artdeco-button--2.artdeco-button--primary")
        accept_button = both_buttons[1]
        accept_button.click()

    def log_me_in(self):
        # Find sign in link and load that page
        sign_in_container = self.driver.find_element_by_class_name('main__sign-in-container')
        sign_in_link = sign_in_container.find_element_by_link_text('Sign in')
        sign_in_link.click()
        sleep(2)  # let website load
        # Find box and enter email address
        email_or_phone_box = self.driver.find_element_by_id('username')
        email_or_phone_box.send_keys(self.username)
        # Find box and enter password
        password_box = self.driver.find_element_by_id('password')
        password_box.send_keys(self.password)
        # Find Sign in button and click
        sign_in_button = self.driver.find_element_by_class_name('btn__primary--large.from__button--floating')
        sign_in_button.click()


def main():
    username = "AiCoreOct2021@outlook.com"
    password = "Password123,,"
    website = "https://www.linkedin.com/feed/"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    scraper = WebDriver(chrome_options, website, username, password)
    scraper.driver.get(website)
    sleep(3)
    scraper.accept_cookies()
    sleep(2)
    scraper.log_me_in()


if __name__ == "__main__":
    # safeguard used to prevent script running
    # automatically if it's imported into another file
    main()
