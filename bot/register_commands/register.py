import os
import requests
import yaml

from utils import COMMANDS_FILENAME, DISCORD_API_URL

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
APPLICATION_ID = os.getenv("APPLICATION_ID")

def register_commands():
    if not DISCORD_BOT_TOKEN or not APPLICATION_ID:
        raise ValueError("Missing TOKEN or APPLICATION_ID in .env file. Please check your configuration.")

    # Load commands from commands.yml
    try:
        print(os.getcwd())
        with open(COMMANDS_FILENAME, "r") as file:
            commands = yaml.safe_load(file)
            if not commands:
                raise ValueError("commands.yml is empty. Add at least one command.")
    except FileNotFoundError:
        raise FileNotFoundError("commands.yml not found. Make sure it exists in the current directory.")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing commands.yml: {e}")

    # Send the POST request for each command
    headers = {
        "Authorization": f"Bot {DISCORD_BOT_TOKEN}",
        "Content-Type": "application/json"
    }

    for command in commands:
        try:
            URL = DISCORD_API_URL.format(APPLICATION_ID=APPLICATION_ID)
            response = requests.post(URL, json=command, headers=headers)
            if response.status_code == 201:
                print(f"Command '{command['name']}' created successfully.")
            else:
                print(
                    f"Failed to create command '{command['name']}': "
                    f"{response.status_code} - {response.json().get('message', 'Unknown error')}"
                )
        except requests.RequestException as e:
            print(f"Error while creating command '{command['name']}': {e}")
