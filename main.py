from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class webdriver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    def __init__(self):
        #TODO: create constructor which initialises webdriver and web adress         
        pass

    def search_term():
        #TODO: create function that searches for a term in the websites search bar and clicks "see all job results button"
        pass
    
    def collect_job_list():
        #TODO: create function that looks for element that contains the list of job postings on the current page
        pass

    def find_next_page():
        #TODO: create function that finds next page element 
        pass
    
