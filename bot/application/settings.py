from os import getenv
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.parent
load_dotenv(BASE_DIR.parent / ".env.example", override=False)
load_dotenv(BASE_DIR.parent / ".env", override=True)

# Bot token
BOT_TOKEN = getenv("BOT_TOKEN")