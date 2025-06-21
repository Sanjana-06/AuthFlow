import os
import django
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from django.conf import settings
from main.tasks import send_welcome_email

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authFlowCore.settings')
django.setup()

from main.models import TelegramUser

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    chat_id = update.effective_chat.id
    TelegramUser.objects.get_or_create(username=username, chat_id=chat_id)
    await update.message.reply_text(f"Hello @{username}, you have been registered!")
    
    # Trigger Celery task
    send_welcome_email.delay(username)

async def run_bot():
    app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(run_bot())
    except KeyboardInterrupt:
        print("Bot stopped.")
