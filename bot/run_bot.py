import os
import discord

from utils import generate_response

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
APPLICATION_ID = os.getenv("APPLICATION_ID")

# Define intents
intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is now connected to Discord!")


# Check the command name and handle accordingly
@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.data["name"] == "hello":
        await interaction.response.send_message(f"Hello, {interaction.user.name}! 👋")

    elif interaction.data["name"] == "echo":
        message = next(
            (option["value"] for option in interaction.data.get("options", []) if option["name"] == "message"),
            "No message provided!"
        )
        await interaction.response.send_message(message)

    elif interaction.data["name"] == "groq":
        message = next(
            (option["value"] for option in interaction.data.get("options", []) if option["name"] == "message"),
            "No message provided!"
        )
        await interaction.response.send_message(generate_response(message=message))

# Run the bot
def run_bot():
    if not DISCORD_BOT_TOKEN:
        raise ValueError("DISCORD_BOT_TOKEN is missing. Check your .env file.")
    bot.run(DISCORD_BOT_TOKEN)
