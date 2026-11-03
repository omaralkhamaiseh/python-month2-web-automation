# User Explorer — REST API Project

A Python command-line application that retrieves user information from a public REST API and allows users to search for specific users by ID.

## Features

- Retrieves user data using HTTP GET requests.
- Parses JSON responses into Python data.
- Displays user IDs, names, emails, and cities.
- Allows searching for a specific user by ID.
- Handles invalid user input and API request errors.
- Uses functions to organize application logic.

## Technologies

- Python
- Requests
- JSON
- REST API

## API

This project uses the free [JSONPlaceholder API](https://jsonplaceholder.typicode.com/users) for demonstration purposes.

## Installation

Install the required Python package:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The application retrieves user information, displays the available users, and prompts you to enter a user ID.

## Learning Outcomes

This project demonstrates practical experience with REST APIs, HTTP requests, JSON parsing, Python functions, dictionaries, loops, and exception handling.