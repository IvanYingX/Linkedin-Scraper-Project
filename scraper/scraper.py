#import all methods from method.py file
from methods import *
from secrets import (LINKEDINUSERNAME,LINKEDINPASSWORD)

def main():
    '''
    Function that controls scraper script
    '''

    website = "https://www.linkedin.com/feed/"
    chrome_options = Options()
    #chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--headless")
    scraper = WebDriver(chrome_options, website, LINKEDINUSERNAME, LINKEDINPASSWORD)
    scraper.driver.implicitly_wait(2)
    scraper.driver.get(website)
    sleep(3)
    scraper.accept_cookies()
    sleep(2)
    scraper.log_me_in()
    sleep(2)
    # Edit this to change search term and location
    scraper.search_term('Data Science', 'United Kingdom')
    sleep(2)
    scraper.extract_job_details()
    sleep(2)
    print("\n\nScraping has been completed")

if __name__ == "__main__":
    # safeguard used to prevent script running
    # automatically if it's imported into another file
    main()
