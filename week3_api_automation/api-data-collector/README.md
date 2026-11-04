# Automated API Data Collector

A Python command-line application that retrieves data from two REST API endpoints, connects posts to their authors, and saves the results in JSON and CSV formats.

## Features

- Retrieves users and posts using HTTP GET requests.
- Matches posts with their authors using user IDs.
- Processes the first 10 posts.
- Saves processed information in JSON and CSV formats.
- Handles API request failures and file-saving errors.
- Uses reusable Python functions.

## Technologies

- Python
- Requests
- JSON
- CSV
- REST APIs

## Data Source

This project uses the free [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) for demonstration purposes.

## Installation

Install the required package:

```bash
pip install -r requirements.txt
```

## Usage

Run the application from the `api-data-collector` directory:

```bash
python main.py
```

The program generates two files inside the `output` folder:

- `posts.json`
- `posts.csv`

Each contains the first 10 posts with their authors' names.

## What I Learned

This project helped me practice reusable Python functions, API integration, JSON parsing, CSV writing, dictionary processing, and exception handling.