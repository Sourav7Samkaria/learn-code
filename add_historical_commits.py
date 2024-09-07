import os
import datetime
from git import Repo

# Define variables
repo_dir = "C:\Users\Lenovo\OneDrive\Desktop\code\learn-code"  # Replace with your repository directory
start_date = datetime.date(2019, 1, 1)  # Start date for commits
end_date = datetime.date(2019, 12, 31)    # End date for commits
file_name = "file.txt"     # File to commit
commit_message = "Historical commit"

# Initialize repository
repo = Repo(repo_dir)
git = repo.git

# Create or modify the file
file_path = os.path.join(repo_dir, file_name)
with open(file_path, 'w') as file:
    file.write("Historical commit")

# Function to generate commits
def make_commits(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        git.add(file_name)
        git.commit(date=f"{current_date}T12:00:00", m=commit_message)
        current_date += datetime.timedelta(days=1)

# Make historical commits
make_commits(start_date, end_date)

# Push changes to GitHub
git.push('origin', 'main')

print("Historical commits added.")
