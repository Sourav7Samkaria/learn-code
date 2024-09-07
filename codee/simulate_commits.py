import os
import subprocess
from datetime import datetime, timedelta

# Configuration
repo_path = r'C:\Users\Lenovo\OneDrive\Desktop\code\codee'  # Replace with the path to your repository
start_date = datetime(2019, 1, 1)
end_date = datetime(2019, 12, 31)
num_commits_per_day = 5  # Number of commits per day

# Prompt for Git configuration
username = input("Enter your Git username: ")
email = input("Enter your Git email: ")

# Set Git configuration for the repository
subprocess.run(['git', 'config', 'user.name', username])
subprocess.run(['git', 'config', 'user.email', email])

# Change to the repository directory
os.chdir(repo_path)

current_date = start_date

while current_date <= end_date:
    for _ in range(num_commits_per_day):
        # Create a new file with a commit message
        file_name = f'file_{current_date.strftime("%Y-%m-%d")}.txt'
        with open(file_name, 'w') as f:
            f.write('This is a simulated commit.')

        # Add the file and commit
        subprocess.run(['git', 'add', file_name])
        commit_message = f'Simulated commit on {current_date.strftime("%Y-%m-%d")}'
        subprocess.run(['git', 'commit', '-m', commit_message])

    # Push changes
    subprocess.run(['git', 'push'])

    # Move to the next day
    current_date += timedelta(days=1)
