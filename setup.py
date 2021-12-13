from setuptools import setup
from setuptools import find_packages

setup(
    name='linkedin_web_scraper',
    version='0.0.1',
    description='Webscraper package that collects specified job data from LinkedIn',
    url='https://github.com/IvanYingX/Linkedin-Scraper-Project',
    author='MateuszBar, armanh3k, JosephSolomon99',
    license='MIT',
    packages=find_packages(),
    install_requires=['selenium', 'webdriver_manager']
)
