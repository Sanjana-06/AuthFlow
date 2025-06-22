import os
import django
import asyncio
import logging
import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from django.conf import settings

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authFlowCore.settings')
django.setup()

from main.models import TelegramUser
from main.tasks import send_welcome_email

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    chat_id = update.effective_chat.id
    TelegramUser.objects.get_or_create(username=username, chat_id=chat_id)
    await update.message.reply_text(f"Hello @{username}, you have been registered!")
    send_welcome_email.delay(username)

async def run_bot():
    app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    # Use run_polling with proper shutdown handling
    try:
        await app.initialize()
        await app.start()
        await app.updater.start_polling()
        
        # Keep the bot running
        while True:
            await asyncio.sleep(1)
            
    except KeyboardInterrupt:
        logging.info("Bot stopped by user")
    except Exception as e:
        logging.error(f"Bot error: {e}")
    finally:
        # Proper shutdown
        try:
            await app.updater.stop()
            await app.stop()
            await app.shutdown()
        except Exception as e:
            logging.error(f"Shutdown error: {e}")

def main():
    # Check if we're in an environment with an existing event loop
    try:
        # Try to get the current event loop
        loop = asyncio.get_running_loop()
        # If we get here, there's already a running loop
        logging.info("Event loop already running, creating task...")
        task = loop.create_task(run_bot())
        return task
    except RuntimeError:
        # No event loop running, we can create one
        logging.info("No event loop running, creating new one...")
        if sys.platform.startswith('win'):
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())     
        try:
            asyncio.run(run_bot())
        except KeyboardInterrupt:
            logging.info("Bot stopped by user")
        except Exception as e:
            logging.error(f"Error running bot: {e}")

if __name__ == '__main__':
    main()