import requests
import json
import csv 
def combine_data(users,posts):
    results=[]
    for post in posts[:10]:
        for user in users:
            if post['userId']==user['id']:
                post_info={
                    "author":user['name'],
                    "title":post['title'],
                }
                results.append(post_info)
                break
    return results
def save_json(data,filename):
    with open(filename,'w',encoding="utf-8") as f:
        json.dump(data,f,indent=4)
def save_csv(data,filename):
    with open(filename,'w',encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=["author","title"])
        writer.writeheader()
        writer.writerows(data)

def fetch(url):
    response=requests.get(url,timeout=10)
   
    response.raise_for_status()
    data=response.json()
    return data
users_url = "https://jsonplaceholder.typicode.com/users"
post_url="https://jsonplaceholder.typicode.com/posts"
try:
    users = fetch(users_url)
    posts = fetch(post_url)
    combined = combine_data(users, posts)
    save_json(combined, "output/posts.json")
    save_csv(combined, "output/posts.csv")
    print(len(combined))
    print(combined[0])
except requests.exceptions.RequestException as e:
    print(f"API error:{e}")
except OSError as e:
    print(f"File saving error:{e}")        