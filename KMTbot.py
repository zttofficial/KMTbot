from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger()

def KMT(bot, update):
    update.message.reply_text("Kuomintang")

def officer(update, context):
    reply = bot.send_sticker(chat_id=update.effective_chat.id,
                             sticker="CAADBQADIwAD4RTDG2se4dhpZE0DFgQ")
    update.message.reply_text(reply)

def main():
    updater = Updater(token='TOKEN', use_context=True)
    
    officer_handler = CommandHandler('officer', officer)
    dispatcher.add_handler(officer_handler)
    updater.dispatcher.add_handler(CommandHandler('KMT', KMT))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
