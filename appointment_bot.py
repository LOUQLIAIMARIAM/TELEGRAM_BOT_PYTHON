import os
import logging
from dotenv import load_dotenv
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton , InlineKeyboardMarkup

from telegram.ext import Application, CommandHandler, CallbackContext

# Load environment variables
load_dotenv()
token = os.getenv("TOKEN")

if not token:
    raise ValueError("Bot token not found. Check your .env file.")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define command handler
async def start(update, context):
    logger.info("Commande /start appelée")
    await update.message.reply_text(
        """
        Bienvenue sur le bot de my_appointement_bot.
        Pour avoir les dernières informations, veuillez faire :
        — /site pour consulter le site
        — /question pour répondre à une question
        — /youtube pour voir les dernières vidéos
        """
    )

async def site(update, context):
    logger.info("Commande /site appelée")
    await update.message.reply_text(
        "Voulez-vous consulter le site https://www.pinterest.com/"
    )

async def question(update: Update, context: CallbackContext):
    logger.info("Commande /question appelée")

    keyboard = [
        [KeyboardButton("Python"), KeyboardButton("Java")],
        [KeyboardButton("JavaScript"), KeyboardButton("C et C++")],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True
    )

    logger.info("Envoi du clavier en cours...")
    await update.message.reply_text(
        "Quel est votre langage préféré ?", reply_markup=reply_markup
    )
    logger.info("Clavier envoyé avec succès.")


async def youtube(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton('Python','https://www.youtube.com/watch?v=h3VCQjyaLws&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ')],
        [InlineKeyboardButton('Java','https://www.youtube.com/watch?v=h3VCQjyaLws&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ')],
        [InlineKeyboardButton('JavaScript','https://www.youtube.com/watch?v=h3VCQjyaLws&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ')],   
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Que voulez-vous apprendre aujourd'hui  ?", reply_markup=reply_markup
    )


if __name__ == "__main__":
    app = Application.builder().token(token).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("site", site))
    app.add_handler(CommandHandler("question", question))
    app.add_handler(CommandHandler("youtube", youtube))

    logger.info("Le bot est démarré.")
    app.run_polling(poll_interval=5, timeout=120)
