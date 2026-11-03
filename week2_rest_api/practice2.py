import requests
url="https://jsonplaceholder.typicode.com/posts?utm_source=chatgpt.com"
params={
    "userId": 3
    }
response=requests.get(url,params=params,timeout=10)
response.raise_for_status()
data=response.json()
for user in data[:5]:
    print(f"Title: {user['title']}")