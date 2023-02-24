# python-telegram-bot==13.15
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
# /start, /komanda
from googletrans import Translator

tarjimon = Translator()

def tarjima(matn, b_til, i_til):
    t_matn = tarjimon.translate(matn, src=b_til, dest=i_til)
    return t_matn



TOKEN = '6044418045:AAGsrn5tB8ZHLw2I8bhWl0uNzzVEhmQqRPo'

def start(update, context):
    ism = update.message.from_user.first_name
    update.message.reply_html(f'<b>{ism}</b>, botimizga xush kelibsiz')
    return 1

def salom(update, context):
    update.message.reply_text('Assalomu aleykum')
    return 2


def translate(update, context):
    matn = update.message.text 
    if matn == '/start':
        start(update, context)
        return 1
    else:
        r = matn.split(',')  # uz,ru,matn
        t_matn = tarjima(r[2], r[0], r[1])
        update.message.reply_text(t_matn.text)    
        return 2


def main():
    updater = Updater(TOKEN, use_context=True)

    disp = updater.dispatcher

    conv_hand = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [
                CommandHandler('salom', salom)
            ],
            2:[
                MessageHandler(Filters.text, translate)
            ]
        },
        fallbacks=[CommandHandler('start', start)]
    )
    disp.add_handler(conv_hand)
    # disp.add_handler(CommandHandler('start', start))
    # disp.add_handler(CommandHandler('salom', salom))
    # disp.add_handler(MessageHandler(Filters.text, translate))

    updater.start_polling()
    updater.idle()


main()