import requests
import json
url="https://jsonplaceholder.typicode.com/users"
response=requests.get(url,timeout=10)
response.raise_for_status()
data=response.json()
results=[]
for user in data[0:5]:
    user_info={
        "name":user['name'],
        "email":user['email']
    }
    results.append(user_info)

with open("users.json","w") as f:
    json.dump(results,f,indent=4)
print(results)