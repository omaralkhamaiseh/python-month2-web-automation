import requests
API_url="https://jsonplaceholder.typicode.com/users"
response=requests.get(API_url,timeout=10)
response.raise_for_status()
data=response.json()
for user in data[:3]:
    print(f"User: {user['id']}")
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"City: {user['address']['city']}")
    print()