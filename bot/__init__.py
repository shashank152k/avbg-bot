# Discord bot's __init__.py

from .run_bot import run_bot
from .register_commands.register import register_commands

__all__ = ["run_bot", "register_commands"]
