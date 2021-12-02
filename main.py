from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class WebDriver():
    def __init__(self,address):   
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) #ChromeDriverManager automates the webdriver install the first time it is run and simply finds it the next time
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
    
