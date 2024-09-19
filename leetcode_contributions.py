import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
import requests
from datetime import datetime

# Function to fetch contributions from LeetCode
def get_leetcode_contributions(username, start_date, end_date):
    # Define the GraphQL query
    query = '''
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            contributions {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            date
                            contributionCount
                        }
                    }
                }
            }
        }
    }
    '''
    
    # LeetCode API URL
    url = 'https://leetcode.com/graphql/'
    
    # Create the request payload with username
    variables = {"username": username}
    
    # Make the POST request to the LeetCode GraphQL API
    response = requests.post(url, json={"query": query, "variables": variables})
    
    # Debugging: Print the full response content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")  # This will show the actual response for debugging
    
    # Check if the request was successful (HTTP status 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()["data"]["matchedUser"]["contributions"]["contributionCalendar"]["weeks"]
        
        # Convert the start and end dates from string to datetime format
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Initialize the total contributions counter
        total_contributions = 0
        
        # Loop through each week and each day to calculate contributions in the given date range
        for week in data:
            for day in week["contributionDays"]:
                day_date = datetime.strptime(day["date"], "%Y-%m-%d")
                if start_date <= day_date <= end_date:
                    total_contributions += day["contributionCount"]
        
        # Output the total contributions in the specified date range
        print(f"Total contributions by {username} from {start_date.date()} to {end_date.date()}: {total_contributions}")
    else:
        # Handle the case when the request fails (non-200 status)
        print(f"Failed to fetch contributions. Status code: {response.status_code}")

# MAIN FUNCTION:
if __name__ == "__main__":
    # Enter your LeetCode username here
    username = "souravsamkaria41"  # Replace this with your actual LeetCode username
    
    # Define the start date (in YYYY-MM-DD format)
    start_date = "2022-01-01"  # Replace this with the actual start date you want to track
    
    # Define the end date (use the current date)
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Call the function with the username and date range
    get_leetcode_contributions(username, start_date, end_date)
