import requests
import yaml
import os


URL = f"https://discord.com/api/v9/applications/{os.getenv('APPLICATION_ID')}/commands"



with open("commands.yaml", "r") as file:
    yaml_content = file.read()

commands = yaml.safe_load(yaml_content)
headers = {"Authorization": f"Bot {os.getenv('TOKEN')}", "Content-Type": "application/json"}

# Send the POST request for each command
for command in commands:
    response = requests.post(URL, json=command, headers=headers)
    command_name = command["name"]
    print(f"Command {command_name} created: {response.status_code}")