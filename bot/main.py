import logging
import os
from dotenv import load_dotenv
from telegram.ext import Application

from bot.handlers import setup_handlers

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN not found in environment variables. Copy .env.example to .env and set your token.")

    app = Application.builder().token(token).build()
    setup_handlers(app)

    logger.info("Svitheia bot is starting...")
    print("Svitheia bot is running. Press Ctrl+C to stop.")
    app.run_polling(allowed_updates=["message"])


if __name__ == "__main__":
    main()
