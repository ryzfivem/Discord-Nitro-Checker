import random
import string
import requests
import json
import os

os.makedirs('Links', exist_ok=True)

with open('success.json', 'w') as f:
    f.write("[\n    \n]")


def generate_random_code(length=16):

    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def check_discord_nitro_link(code):

    url = f"https://discord.gift/{code}"
    api_url = f"https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(api_url)

    if response.status_code == 200:
        print(f"\033[92m✅ | {url}\033[0m")
        save_to_success_file(url)
        return True
    else:
        print(f"\033[92m❌ | {url}\033[0m")
        return False

def save_to_success_file(valid_link):

    try:
        with open("success.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(valid_link)

    with open("success.json", "w") as file:
        json.dump(data, file, indent=4)

def main():

    print("Discord Nitro Link Checker gestartet...")
    for _ in range(10000000000000000000000000000000): 
        code = generate_random_code()
        check_discord_nitro_link(code)

if __name__ == "__main__":
    main()
