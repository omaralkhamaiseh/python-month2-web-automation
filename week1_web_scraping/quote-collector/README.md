# Quote Collector

A Python web scraping application that collects quotes and their authors from [Quotes to Scrape](https://quotes.toscrape.com/) and saves them to a text file.

## Features

- Retrieves quotes using HTTP requests.
- Parses HTML using BeautifulSoup.
- Extracts quotes and their authors.
- Saves 10 quotes into `quotes.txt`.
- Checks for HTTP errors.

## Technologies

- Python
- Requests
- BeautifulSoup4

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The program creates a `quotes.txt` file containing the extracted quotes and their authors.

## Project Structure

```text
quote-collector/
├── main.py
├── requirements.txt
├── README.md
└── quotes.txt
```

## Learning Outcomes

This project demonstrates practical experience with HTTP requests, HTML parsing, Python functions, dictionaries, lists, file handling, and basic error detection.