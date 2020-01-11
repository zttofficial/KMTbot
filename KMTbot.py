from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

updater = Updater(token='TOKEN', use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def officer(update, context):
    context.bot.sendSticker(chat_id=update.effective_chat.id,
                             sticker="CAADBQADIwAD4RTDG2se4dhpZE0DFgQ")

def main():
    officer_handler = CommandHandler('officer', officer)
    dispatcher.add_handler(officer_handler)

if __name__ == '__main__':
    main()
