#import all methods from method.py file
from methods import *
 

def main():
    '''
    Function that controls scraper script
    '''
    username = "aicorebot2@outlook.com"
    password = "aicoreteam2"
    website = "https://www.linkedin.com/feed/"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("--headless")
    scraper = WebDriver(chrome_options, website, username, password) 
    scraper.driver.implicitly_wait(2)
    scraper.driver.get(website)
    sleep(3)
    scraper.accept_cookies()
    sleep(2)
    scraper.log_me_in()
    sleep(2)
    scraper.search_term('Data Science', 'London')
    sleep(2)
    scraper.extract_job_details()
    sleep(2)
    #scraper.dataframe_to_csv(my_dataframe)
    print("\n\nScraping has been completed")
if __name__ == "__main__":
    # safeguard used to prevent script running
    # automatically if it's imported into another file
    main()
    

# username = "aicorebot2@outlook.com"
# password = "aicoreteam2"
# username = "AiCoreOct2021@outlook.com"
# password = "Password123,,"