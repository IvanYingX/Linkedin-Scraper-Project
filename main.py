from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options


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
        # TODO: create function that finds accept cookies element
        pass

    def log_me_in():
        # TODO: create function that logs user in with necessary credentials
        pass


def main():
    username = "AiCoreOct2021@outlook.com"
    password = "Password123,,"
    website = "https://www.linkedin.com/feed/"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    scraper = WebDriver(chrome_options, website, username, password)
    scraper.driver.get(website)
    sleep(5)
    scraper.driver.close()


if __name__ == "__main__":
    # safeguard used to prevent script running
    # automatically if it's imported into another file
    main()
