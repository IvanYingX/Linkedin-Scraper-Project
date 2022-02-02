FROM python:3.9.10-slim-buster

COPY . .

RUN python setup.py install

CMD ["python", "scraper/scraper.py"]
