from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class WebDriver():
    '''
    WebDriver class used to move through a website and find elements inside

    Attributes:
        address (str): The address of the website that will be scraped
        username (str): The username for the account on the website
        password (str): The password for the account on the website
        driver : webdriver instance
    '''

    def __init__(self, chrome_options, address: str, username: str, password: str):
        # ChromeDriverManager installs webdriver into cache automatically
        self.address = address
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def search_term(self, job: str, location: str):
        '''
        Function that uses the search bar to search for a term and a location.

        Args:
            job (str): term that we are searching for
            location (str): geographical location where we want to search for jobs

        Returns:
            webpage with results from search
        '''

        job_buttons = self.driver.find_elements_by_class_name('global-nav__icon')
        job_button = job_buttons[2]
        job_button.click()

        sleep(2)
        # search_box = self.driver.find_element_by_class_name('jobs-search-box__text-input.jobs-search-box__keyboard-text-input')
        search_box = self.driver.find_elements_by_class_name('jobs-search-box__text-input')[0]
        search_box.send_keys(job)

        location_box = self.driver.find_elements_by_class_name('jobs-search-box__text-input')[3]
        location_box.send_keys(location)

        search_button = self.driver.find_element_by_class_name('jobs-search-box__submit-button.artdeco-button.artdeco-button--2.artdeco-button--secondary')
        search_button.click()

    def collect_job_list(self):
        '''
        Function that collects hyperlinks of job listings from the current page (only partially working)

        Args:
            None

        Returns:
            list of hyperlinks
        '''
        # finding path to job container
        application_outlet = self.driver.find_element_by_class_name("application-outlet ")
        authenitaction_outlet = application_outlet.find_element_by_class_name("authentication-outlet")
        job_search_ext = authenitaction_outlet.find_element_by_class_name("job-search-ext")
        two_pane_wrapper = job_search_ext.find_element_by_class_name("jobs-search-two-pane__wrapper")
        left_pane = two_pane_wrapper.find_element_by_class_name("jobs-search__left-rail")
        container = left_pane.find_element_by_tag_name("ul")
        jobs = container.find_elements_by_tag_name("li")
        # create set for emberID's relating to each job listing tile in the container
        ember_ids = set()
        for job in jobs:
            # extract emberID from each tile
            job_id = job.get_attribute("id")
            if job_id == "":
                pass
            else:
                # emberID for link is usually 7 higher than the ID for the job listing tile so we augment it and add to set
                num = job_id.strip("ember")
                number = int(num)
                number += 7
                augmented_id = "ember" + str(number)
                ember_ids.add(augmented_id)
        print(ember_ids)
        links = []
        # Go through all emberID's in the set and try to collect link
        for id in ember_ids:
            try:
                element = self.driver.find_element_by_id(id)
                link = element.get_attribute("href")
                links.append(link)
            except NoSuchElementException:
                pass
        # print links for now
        print(links)

    def find_next_page(self):
        '''
        Function that finds the next page of results. Finds total number of search results, gets current URL, appends URL which causes next page to load

        Args:
            None

        Returns:
            next page of search results
        '''

        # finds total number of job results and saves value as integer
        results = self.driver.find_elements_by_class_name('jobs-search-results-list__text')[1].text
        result = int(''.join(c for c in results if c.isdigit()))
        base_url = self.get_current_url()

        # linkedin displays maximum of 40 pages of 25 results, thus any results after the initial 1000 will be ignored
        if result > 975:
            for page in range(25, 1000, 25):
                url = base_url + f"&start={page}"
                print(url)

        elif result <= 975:
            pages = -(-result // 25)  # round number up expression
            for page in range(25, 25 * pages, 25):
                url = base_url + f"&start={page}"
                print(url)

    def get_current_url(self):
        '''
        Function that returns current URL of webdriver

        Args:
            None

        Returns:
            URL (str) : URL of current webpage
        '''
        URL = self.driver.current_url
        return URL

    def accept_cookies(self):
        '''
        Function that finds manage cookies and accept cookies buttons by
        class name and then clicks the accept cookies button
        '''
        # Find both buttons using class_name rather than XPATH
        both_buttons = self.driver.find_elements_by_class_name("artdeco-global-alert-action.artdeco-button.artdeco-button--inverse.artdeco-button--2.artdeco-button--primary")
        accept_button = both_buttons[1]
        accept_button.click()

    def log_me_in(self):
        '''
        Function that finds sign in link, clicks it,
        finds email and password boxes and fills in information
        clicks sign in button

        Args:
            None

        Returns:
            Home webpage where user is logged in
        '''
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
    '''Function that controls whole script'''
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
    sleep(2)
    scraper.search_term('Data Science', 'London')
    sleep(2)
    scraper.collect_job_list()

if __name__ == "__main__":
    # safeguard used to prevent script running
    # automatically if it's imported into another file
    main()
    