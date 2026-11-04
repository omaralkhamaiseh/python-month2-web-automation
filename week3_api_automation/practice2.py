import requests
import csv
url="https://jsonplaceholder.typicode.com/users"
response=requests.get(url,timeout=10)
response.raise_for_status()
data=response.json()
results=[]
for user in data[:5]:
    user_info={
    "name":user['name'],
    "email":user['email'],
    "city":user['address']['city'],
    }
    results.append(user_info)
with open("users.csv","w",encoding="utf-8") as file:
    writer=csv.DictWriter(file,fieldnames=["name","email","city"] )
    writer.writeheader()
    writer.writerows(results)