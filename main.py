from bot import register_commands, run_bot
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

if __name__ == "__main__":
    register_commands()
    run_bot()
