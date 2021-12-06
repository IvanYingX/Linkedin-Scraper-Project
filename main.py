from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver():
    '''
    WebDriver class used to move through a website and find elements inside

    Attributes:
        address (str): The address of the website that will be scraped 
    '''
    def __init__(self,address:str):   
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) #ChromeDriverManager installs webdriver into cache automatically
        self.address = address

    def search_term():
        #TODO: create function that searches for a term in the websites search bar and clicks "see all job results button"
        pass
    
    def collect_job_list():
        #TODO: create function that looks for element that contains the list of job postings on the current page
        pass

    def find_next_page():
        #TODO: create function that finds next page element 
        pass

    def previous_page():
        #TODO: create function that finds the previous page element
        pass

    def current_url():
        #TODO: create function that finds the current page url
        pass

    def AcceptCookies():
        #TODO: create function that finds accept cookies element
        pass

def main():
    pass

if __name__ == "__main__": #safeguard used to prevent script running automatically if it's imported into another file
    main()
