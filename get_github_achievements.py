import requests

def get_github_user_data(username):
    user_url = f'https://api.github.com/users/{username}'
    user_response = requests.get(user_url)
    
    if user_response.status_code == 200:
        user_data = user_response.json()
        print("GitHub User Data:")
        print(user_data)
    else:
        print(f"Error fetching user data: {user_response.status_code} - {user_response.text}")

def main():
    username = input("Enter GitHub username: ")
    email = input("Enter your email: ")
    
    # Placeholder for validating email
    if '@' in email:  # Simple validation check
        print(f"Email '{email}' looks valid.")
    else:
        print("Invalid email format.")
        return
    
    try:
        get_github_user_data(username)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
