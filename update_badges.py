import os
import subprocess

def get_user_input():
    username = input("Enter your GitHub username: ")
    email = input("Enter your email: ")
    return username, email

def update_readme(username, email):
    readme_path = "README.md"
    badges = [
        f"![GitHub followers](https://img.shields.io/github/followers/{username}?style=social)",
        f"![GitHub stars](https://img.shields.io/github/stars/{username}?style=social)",
        f"![Twitter Follow](https://img.shields.io/twitter/follow/{username}?style=social)",
        f"![LinkedIn](https://img.shields.io/badge/LinkedIn-{username}-blue)"
    ]

    with open(readme_path, "w") as file:
        file.write(f"# {username}\n\n")
        for badge in badges:
            file.write(f"{badge}\n")
        file.write(f"\nEmail: [{email}](mailto:{email})\n")

def commit_and_push():
    try:
        subprocess.run(["git", "add", "README.md"], check=True)
        subprocess.run(["git", "commit", "-m", "Update README with badges"], check=True)
        subprocess.run(["git", "push", "origin", "master"], check=True)
        print("Badges updated successfully in your GitHub profile README.")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")

def main():
    username, email = get_user_input()
    update_readme(username, email)
    commit_and_push()

if __name__ == "__main__":
    main()
