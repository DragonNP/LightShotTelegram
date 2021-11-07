import logging
import lightshot
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Logger setup
import secrets

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

isSortPhoto = False


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            KeyboardButton('Рандомная фотка'),
        ],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text('Это LightShot бот', reply_markup=reply_markup)


def send_random_photo(update: Update, context: CallbackContext) -> None:
    isRandPhoto = True
    while isRandPhoto:
        url = lightshot.get_random_image_url()
        if not url:
            continue
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)
        isRandPhoto = False


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(token=secrets.BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.regex('Рандомная фотка'), send_random_photo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
