
import os
import subprocess
from datetime import datetime, timedelta
import random

# Ask for user input
user_name = input("Enter your GitHub username: ")
user_email = input("Enter your GitHub email: ")

# Update this path to your Git repository
repo_path = 'C:/Users/Lenovo/OneDrive/Desktop/code/learn-code'

# List of short, professional commit messages
commit_messages = [
    'Fix Python error handling',
    'Optimize React renders',
    'Update MUI button styles',
    'Refactor Tailwind classes',
    'Fix TypeScript API types',
    'Improve Jest coverage',
    'Enhance Axios error handling',
    'Update useState usage',
    'Refactor API calling',
    'Fix Tailwind grid layout',
    'Update React context',
    'Add TypeScript interfaces',
    'Improve Storybook setup',
    'Optimize Python script',
    'Fix MUI validation issues',
    'Refactor JS async functions',
    'Update Jest snapshots',
    'Enhance Axios config',
    'Fix useState issues',
    'Improve Tailwind spacing',
    'Refactor TypeScript utils',
    'Update Python packages',
    'Fix MUI component styles',
    'Enhance Axios responses',
    'Refactor Jest setup',
    'Optimize Tailwind config',
    'Fix TypeScript API errors',
    'Improve Jest component tests',
    'Update MUI theme',
    'Refactor Axios logic',
    'Fix useState updates',
    'Enhance Python logging',
    'Update Storybook stories',
    'Fix React prop types',
    'Optimize Tailwind utilities',
    'Update MUI form styles',
    'Refactor Python data handling',
    'Improve API response parsing',
    'Fix TypeScript type errors',
    'Enhance Jest mocks',
    'Update Axios request logic',
    'Fix React useEffect bugs',
    'Refactor Tailwind color schemes',
    'Improve Python script efficiency',
    'Update Jest configuration',
    'Fix MUI input validation',
    'Enhance Axios request handling',
    'Refactor React state management',
    'Update TypeScript config',
    'Fix Tailwind responsive design',
    'Optimize Python package imports',
    'Improve React component performance',
    'Fix MUI layout issues',
    'Enhance Jest test cases',
    'Update Axios interceptors',
    'Refactor useState logic',
    'Fix TypeScript generics',
    'Improve Tailwind spacing utilities',
    'Update React hooks',
    'Fix Python script bugs',
    'Enhance MUI modal styles',
    'Refactor Axios error handling',
    'Update TypeScript functions',
    'Fix Jest test failures',
    'Improve React component styles',
    'Optimize Tailwind animations',
    'Fix Python package dependencies',
    'Update MUI table styles',
    'Refactor API response handling',
    'Improve Jest test coverage',
    'Fix React context issues',
    'Update Axios configuration',
    'Refactor Tailwind breakpoints',
    'Fix TypeScript import errors',
    'Enhance Python logging',
    'Update Storybook addons',
    'Improve React performance',
    'Fix MUI dropdown issues',
    'Optimize Tailwind layout',
    'Refactor Jest mocks',
    'Update TypeScript types',
    'Fix Python function errors',
    'Enhance React hooks',
    'Update MUI theme settings',
    'Fix Tailwind utility classes',
    'Improve Axios response handling',
    'Refactor TypeScript interfaces',
    'Update React component tests',
    'Fix Python error messages',
    'Enhance MUI button functionality',
    'Refactor Tailwind typography',
    'Update Axios instance',
    'Fix TypeScript errors',
    'Improve React useEffect',
    'Optimize Python code',
    'Update MUI card styles',
    'Refactor Tailwind grid',
    'Fix Jest snapshot issues',
    'Enhance React state updates',
    'Update TypeScript utils',
    'Fix MUI dialog bugs',
    'Improve Tailwind colors',
    'Refactor API error handling',
    'Update React component logic',
    'Fix Python performance issues',
    'Enhance MUI icon styles',
    'Refactor Tailwind utilities',
    'Update Axios error handling',
    'Fix TypeScript configurations',
    'Improve React performance',
    'Update MUI theme colors',
    'Refactor Python functions',
    'Fix Tailwind spacing',
    'Enhance Jest test setup',
    'Update React context API',
    'Refactor MUI components',
    'Fix Axios response bugs',
    'Improve TypeScript generics',
    'Update Tailwind breakpoints',
    'Refactor Python script logic',
    'Fix React component bugs',
    'Enhance MUI styles',
    'Update Axios requests',
    'Fix TypeScript issues',
    'Improve React performance',
    'Update Tailwind utilities',
    'Refactor Jest configuration',
    'Fix MUI form bugs',
    'Enhance Python code readability',
    'Update React state management',
    'Fix Axios configuration',
    'Improve Tailwind responsiveness',
    'Refactor TypeScript types',
    'Update MUI layout',
    'Fix Python package issues',
    'Enhance React context',
    'Update Tailwind styles',
    'Refactor Jest tests',
    'Fix Axios bugs',
    'Improve MUI components',
    'Update TypeScript functions',
    'Fix React UI issues',
    'Enhance Python scripts',
    'Refactor Tailwind code',
    'Update Jest coverage',
    'Fix TypeScript errors',
    'Improve Axios handling',
    'Update MUI configurations',
    'Refactor React components',
    'Fix Tailwind design issues'
]

# Change to the Git repository directory
os.chdir(repo_path)

# Function to create a commit
def create_commit(date_str, commit_message):
    # Set Git username and email
    subprocess.run(['git', 'config', 'user.name', user_name])
    subprocess.run(['git', 'config', 'user.email', user_email])

    # Create or update a file for committing
    file_path = os.path.join(repo_path, 'contribution.txt')
    with open(file_path, 'a') as file:
        file.write(f'Commit on {date_str}\n')

    # Add the file to staging
    subprocess.run(['git', 'add', file_path])

    # Commit with the given date
    subprocess.run(['git', 'commit', '--date', date_str, '-m', commit_message])

def main():
    # Start date: January 1, 2021
    start_date = datetime(2021, 1, 1)
    # End date: Current date
    end_date = datetime.now()

    # Get the total number of days between start and end dates
    total_days = (end_date - start_date).days

    # Generate 500 random dates and create commits
    for _ in range(800):
        day_offset = random.randint(0, total_days)
        current_date = start_date + timedelta(days=day_offset)
        date_str = current_date.strftime('%Y-%m-%d')

        # Choose a random commit message
        commit_message = random.choice(commit_messages)

        # Create a commit for this date
        create_commit(date_str, commit_message)

if __name__ == '__main__':
    main()
