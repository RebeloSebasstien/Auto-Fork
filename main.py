import requests
import time
import os
import platform
from colorama import Fore, Style, init


init(autoreset=True)
api = "https://api.github.com"
session = "session"

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def save(username, token):
    
    with open(session, "w") as file:
        file.write(f"{username}\n{token}")

def load():
    if os.path.exists(session):
        with open(session, "r") as file:
            l = file.readlines()
            return l[0].strip(), l[1].strip()
    return None, None

def check(username, token):
    headers = {"Authorization": f"token {token}"}
    response = requests.get(f"{api}/user", headers=headers)
    return response.status_code == 200

def login():
    username, token = load()
    if username and token:
        if check(username, token):
            return username, token
        else:
            print(f"{Fore.RED}You got logged out. Please log in again.")

    while True:
        clear()
        print(f"{Fore.CYAN}Login")
        username = input("Username: ")
        token = input("GitHub Token: ")
        if check(username, token):
            save(username, token)
            print(f"{Fore.GREEN}Login successful!")
            time.sleep(1)
            clear()
            return username, token
        else:
            print(f"{Fore.RED}Invalid credentials. Please try again.")
            time.sleep(2)

def search(keywords, token, pages):
    headers = {
        "Authorization": f"token {token}",
    }
    params = {
        "q": keywords,
        "per_page": pages,  # Number of repositories per page
        "sort": "stars",
        "order": "desc",
    }
    response = requests.get(f"{api}/search/repositories", headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"{Fore.RED}Error: {response.status_code} - {response.json().get('message')}")
        return []

def fork(r, token):
    headers = {
        "Authorization": f"token {token}",
    }
    response = requests.post(f"{api}/repos/{r}/forks", headers=headers)

    if response.status_code == 202:
        print(f"{Fore.GREEN}Forked: {r}")
        return True
    else:
        print(f"{Fore.RED}Failed to fork: {r} - {response.json().get('message')}")
        return False

def main():
    username, token = login()

    while True:
        clear()
        print(f"{Fore.BLUE}Welcome, {username}!")
        print(f"{Style.BRIGHT}1. Fork")
        print(f"{Style.BRIGHT}2. Exit")
        choice = input(f"{Fore.YELLOW}Enter your choice: {Style.RESET_ALL}")

        if choice == "1":
            keywords = input(f"{Fore.CYAN}Search: {Style.RESET_ALL}")
            pages = input(f"{Fore.CYAN}How many repositories: {Style.RESET_ALL}")

            print(f"{Fore.BLUE}Searching...")
            repositories = search(keywords, token, pages)

            if not repositories:
                print(f"{Fore.RED}No repositories found.")
                input(f"{Fore.YELLOW}Press Enter to return to the menu...")
                continue

            print(f"{Fore.GREEN}{len(repositories)} repositories found.")
            for repo in repositories:
                print(f"- {Fore.MAGENTA}{repo['full_name']}")

            fork_choice = input(f"{Fore.YELLOW}Do you wish to fork them? (y/n): {Style.RESET_ALL}").strip().lower()

            if fork_choice == "y":
                print(f"{Fore.BLUE}Starting to fork...")
                forked_repos = []

                for repo in repositories:
                    r = repo["full_name"]
                    print(f"Forking repository: {Fore.MAGENTA}{r}")
                    if fork(r, token):
                        forked_repos.append(r)
                    time.sleep(2)  # To avoid hitting API rate limits

                print(f"\n{Fore.GREEN}Forking completed.")
                if forked_repos:
                    print(f"{Fore.CYAN}Forked Repositories:")
                    for repo in forked_repos:
                        print(f"- {Fore.MAGENTA}{repo}")
                else:
                    print(f"{Fore.RED}No repositories were forked.")
                input(f"{Fore.YELLOW}Press Enter to return to the menu...")
            else:
                print(f"{Fore.YELLOW}Skipping forking.")
                input(f"{Fore.YELLOW}Press Enter to return to the menu...")

        elif choice == "2":
            print(f"{Fore.GREEN}Exiting the program. Goodbye!")
            break

        else:
            print(f"{Fore.RED}Invalid choice. Please try again.")
            time.sleep(2)

if __name__ == "__main__":
    main()
