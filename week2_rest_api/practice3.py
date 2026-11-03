import requests
url = "https://jsonplaceholder.typicode.com/posts/999999"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data=response.json()
    print(data['title'])
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")