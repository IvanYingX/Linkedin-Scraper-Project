# Linkedin-Scraper-Project

A selenium based web scraper that scrapes job advertisement data from Linkedin. 
Can search for any job and location, scrapes all 40 visible pages and sends data to your configured AWS RDS endpoint.

## Installation

This is a docker containerised application, to use it simply run the following code in a terminal:

```bash
docker run --rm -it aicoreoct/linkedin_scraper:latest
```
## Usage

Before using, you will need the following details:

#LinkedIn login details
LINKEDINUSERNAME = ''
LINKEDINPASSWORD = ''

#Database info
DATABASE_TYPE = '' 
DBAPI = ''
ENDPOINT = '' #AWS Endpoint
USER = ''
PASSWORD = ''
PORT= ''
DATABASE= ''

After running the docker run command above, the container will start and it will ask you to input all of the information above. After it has done that it will ask for a job title and location to scrape. Sends data one page at a time. It will notify you after each webpage it scrapes.

## License
[MIT](https://choosealicense.com/licenses/mit/)