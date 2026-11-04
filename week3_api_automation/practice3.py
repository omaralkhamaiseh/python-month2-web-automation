import requests
userAPI="https://jsonplaceholder.typicode.com/users"
postAPI="https://jsonplaceholder.typicode.com/posts"
Uresponse=requests.get(userAPI,timeout=10)
presponse=requests.get(postAPI,timeout=10)
Uresponse.raise_for_status()
presponse.raise_for_status()
user_data=Uresponse.json()
post_data=presponse.json()
for post in post_data[:5]:
    for user in user_data:
        if  post['userId'] == user['id']:
            print(f"Author: {user['name']}")
            print(f"Title: {post['title']}")
            print()
            break
