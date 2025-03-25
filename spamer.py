import time
import random
import requests


# List of random messages to send
MESSAGES = [
    "Hello there!",
    "How's your day going?",
    "Stay safe and take care!",
    "Random message incoming!",
    "Hope you’re having a great time!",
    "Just a friendly bot saying hi!",
    "Keep up the good work!",
    "What’s new today?"
]

# Function to read the token and channel IDs from the file
def read_tokens(file_path):
    with open(file_path, "r") as file:
        return [line.strip().split(":") for line in file]
    
def spam(channel_id, tk):
    try:
        session = requests.session()
        url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
        headers = {
            "Authorization": f"{tk}",  # Bot token with 'Bot ' prefix
        }
        payload = {
            "content": random.choice(MESSAGES),  # Send a random message
            "tts": False
        }

        # Send the message
        res = requests.post(url, json=payload, headers=headers)
        if res.status_code not in (200, 201, 204):
            print(f"\033[1;31mFailed to send message: {res.text}\033[0m")
            return
    except requests.RequestException as e:
        print(f"\033[1;31mAn error occurred: {e}\033[0m")

# Function to continuously run the script
def run_script():
    while True:
        # Read tokens at the beginning of each round
        tokens = read_tokens("tokens.txt")

        # Iterate over each token,
        for channel_id, tk in tokens:
            spam(channel_id, tk)
            
            # Random delay between 5 to 8 minutes
            delay = random.randint(300, 480)
            print(f"\033[1;34mNext message in {delay // 60} minutes...\033[0m")
            time.sleep(delay)  

try:
    run_script()
except KeyboardInterrupt:
    print("\033[1;92mScript terminated.\033[0m")
