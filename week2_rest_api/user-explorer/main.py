import requests
API_url="https://jsonplaceholder.typicode.com/users"
def fetch_users():
    response=requests.get(API_url,timeout=10)
    response.raise_for_status()
    data=response.json()
    return data
def display_users(users):
    for user in users:
        print(f"User ID:{user['id']}")
        print(f"Name:{user['name']}")
        print(f"Email:{user['email']}")
        print(f"City:{user['address']['city']}")
        print()
def find_user(users,user_id):
    for user in users:
        if user['id']==user_id:
            print(f"Name:{user['name']}")
            print(f"Email:{user['email']}")
            print(f"City:{user['address']['city']}")
            print()
            return 
    print(f"No user found with ID {user_id}") 
try:
    users = fetch_users()
    display_users(users)
    user_id=int(input("Enter a user ID:"))
    find_user(users,user_id)
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching users: {e}")  
except ValueError:
    print("Invalid input. Please enter a valid integer for user ID.")