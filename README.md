# Linkedin-Scraper-Project

A selenium based web scraper that scrapes job advertisement data from Linkedin. 
Can search for any job and location, scrapes all 40 visible pages and sends data to AWS RDS.

## Installation

Use the package manager [pip](https://pypi.org/) and search for linkedin_web_scraper to install whole package.

OR 

```bash
pip install linkedin_web_scraper
```

## Usage

Before using, configure the following:
Change __main__.py code with appropriate details for your LinkedIn login
Change methods.py send_data_to_aws method to your database details
Change search terms in __main__.py

Usage:
Run __main__.py and use a postgresql relation database manager to view and query scraped data.

## Contributing
No contributions welcome, thank you

## License
[MIT](https://choosealicense.com/licenses/mit/)