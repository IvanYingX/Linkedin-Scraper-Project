from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
#from sqlalchemy import create_engine
import pandas as pd 
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
        # self.driver = webdriver.Chrome(options=chrome_options)



    def get_current_url(self):
        '''
        Method that returns current URL of webdriver

        Args:
            None

        Returns:
            URL (str) : URL of current webpage
        '''
        URL = self.driver.current_url
        return URL



    def accept_cookies(self):
        '''
        Method that finds manage cookies and accept cookies buttons by
        class name and then clicks the accept cookies button
        '''
        # Find both buttons using class_name rather than XPATH
        both_buttons = self.driver.find_elements_by_class_name("artdeco-global-alert-action.artdeco-button.artdeco-button--inverse.artdeco-button--2.artdeco-button--primary")
        accept_button = both_buttons[1]
        accept_button.click()



    def log_me_in(self):
        '''
        Method that finds sign in link, clicks it,
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




    def search_term(self, job: str, location: str):
        '''
        Method that uses the search bar to search for a term and a location.

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



    def find_all_pages(self):
        '''
        Method that finds the next page of results. Finds total number of search results, gets current URL, appends URL which causes next page to load

        Args:
            None

        Returns:
            next page of search results
        '''

        # finds total number of job results and saves value as integer
        results = self.driver.find_elements_by_class_name('jobs-search-results-list__text')[1].text
        result = int(''.join(c for c in results if c.isdigit()))
        base_url = self.get_current_url()
        all_pages = []

        # linkedin displays maximum of 40 pages of 25 results, thus any results after the initial 1000 will be ignored
        if result > 975:
            for page in range(25, 1000, 25):
                url = base_url + f"&start={page}"
                all_pages.append(url)

        elif result <= 975:
            pages = (result // 25)  # round number up expression
            for page in range(25, 25 * pages, 25):
                url = base_url + f"&start={page}"
                all_pages.append(url)
        return all_pages




    def pd_from_list(self, list1, list2, list3, list4, list5, list6):
        df = {'Job_title':list1,
                'Company_name':list2,
                'Company_location':list3,
                'Job_detail':list4,
                'Job_description':list5,
                'Job_link':list6}
        dataframe = pd.DataFrame.from_dict(df, orient='index')
        return dataframe.transpose()

    def extract_job_details(self):
        '''
        Method that collects job details from the current searched terms, collects all 40 pages from linkedin results 
        Args:
            None

        Returns:
            Pandas dataframe with scraped data
        '''
        # finding path to job container
        all_pages = self.find_all_pages()
        sleep(1)

        # loop through each page
        for page in range(len(all_pages)): 
            sleep(0.2)
            container = self.driver.find_element_by_class_name("jobs-search-results__list")
            jobs = container.find_elements_by_class_name("jobs-search-results__list-item")
            # create lists which will append important job details for each job scraped
            link_list = []
            job_title_list = []
            company_name_list = []
            company_location_list = []
            job_description_list = []
            job_detail_list = []

            # loop through each job on given page
            for job in jobs:
                try:
                    sleep(0.2)
                    job.click()
                    sleep(0.2)
                    job_panel = self.driver.find_element_by_class_name("job-view-layout.jobs-details")
                    job_title = job_panel.find_element_by_tag_name("h2").text
                    job_title_list.append(job_title)
                    company_details = job_panel.find_element_by_class_name("jobs-unified-top-card__subtitle-primary-grouping")
                    company_name = company_details.find_element_by_tag_name("a").text
                    company_name_list.append(company_name)
                    company_location = company_details.find_element_by_class_name("jobs-unified-top-card__bullet").text
                    a_tag = job_panel.find_element_by_tag_name("a")
                    company_location_list.append(company_location)
                    job_links = a_tag.get_attribute('href')
                    link_list.append(job_links)
                    job_description = job_panel.find_element_by_id("job-details")
                    job_description = job_description.find_element_by_tag_name("span").text
                    job_description_list.append(job_description)
                    ul_tag = job_panel.find_element_by_tag_name("ul")
                    li_tag = ul_tag.find_element_by_class_name("jobs-unified-top-card__job-insight")
                    job_detail = li_tag.find_element_by_tag_name("span").text
                    job_detail_list.append(job_detail)
                except (StaleElementReferenceException,NoSuchElementException):
                    pass
            self.driver.get(all_pages[page])
        # return scraped data through a pandas dataframe
        data_frame = self.pd_from_list(job_title_list,company_name_list,company_location_list,job_detail_list,job_description_list,link_list)
        return data_frame
    
    
    def dataframe_to_csv(self, dataframe: pd.DataFrame):
        '''
        Method that creates a csv file called output_data.csv from a pandas dataframe
        
        Arguments:
            pd.DataFrame
        
        Returns:
            csv file with input data inside

        '''
        dataframe.to_csv('output_data.csv', index=False, header=True, encoding='utf-8')
