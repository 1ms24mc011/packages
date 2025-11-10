import requests
import numpy as np

def get_random_number():
    # returns a random integer
    number = np.random.randint(1, 100)
    return number

def fetch_data():
    response = requests.get("https://api.github.com")
    return response.status_code

if __name__ == "__main__":
    print("Generating a random number...")
    print("Random Number:", get_random_number())

    print("\nChecking GitHub API status...")
    status = fetch_data()
    print("GitHub Status Code:", status)
