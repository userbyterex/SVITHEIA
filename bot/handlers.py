from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from bot.conversation import handle_scientific_question


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome = (
        "Welcome to *Svitheia*.\n\n"
        "I am an autonomous scientific discovery system focused on "
        "hypothesis generation, experimentation, and active falsification.\n\n"
        "Send me a simple scientific question about classical mechanics "
        "(forces, mass, acceleration, projectiles, etc.) and I will run "
        "the full discovery loop.\n\n"
        "Example:\n"
        "`How does mass affect acceleration when force is constant?`"
    )
    await update.message.reply_text(welcome, parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "*Available commands:*\n"
        "/start – Introduction\n"
        "/help – Show this help\n\n"
        "Just send a scientific question in plain English to start a discovery loop."
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    user_text = update.message.text.strip()
    await handle_scientific_question(update, context, user_text)


def setup_handlers(app: Application):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
