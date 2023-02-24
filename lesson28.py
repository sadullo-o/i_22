# python-telegram-bot==13.15
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
# /start, /komanda
from googletrans import Translator


UZRU = 'O\'zbekcha-Inglizcha'
RUEN = 'Ruscha-Inglizcha'
ENRU = 'Inglizcha-Ruscha'

ORTGA = '◀️ ORTGA'

lan_btns = ReplyKeyboardMarkup(
    [
        [UZRU, RUEN],
        [ENRU]
    ], resize_keyboard=True
)

back_btn = ReplyKeyboardMarkup(
    [
    [ORTGA]
    ], resize_keyboard=True
)


test_buttons = [
    [
        InlineKeyboardButton('Test1', callback_data='test1'),
        InlineKeyboardButton('Test2', callback_data='test2'),
    ],
    [
        InlineKeyboardButton('Test3', callback_data='test3'),
        InlineKeyboardButton('Test4', callback_data='test4'),
    ],

]


def tarjima(matn, b_til, i_til):
    tarjimon = Translator()
    t_matn = tarjimon.translate(matn, src=b_til, dest=i_til)
    return t_matn



TOKEN = '6044418045:AAGsrn5tB8ZHLw2I8bhWl0uNzzVEhmQqRPo'

def start(update, context):
    ism = update.message.from_user.first_name
    update.message.reply_html(f'<b>{ism}</b>, botimizga xush kelibsiz', reply_markup=lan_btns)
    return 1

def salom(update, context):
    update.message.reply_text('Assalomu aleykum', reply_markup=InlineKeyboardMarkup(test_buttons))
    return 'call'



def ruseng(update,context):
    global til1
    global til2
    update.message.reply_text('Ruscha matn kiriting', reply_markup=back_btn)
    til1 = 'ru'
    til2 = 'en'
    return 'TARJIMA'

def uzbru(update,context):
    global til1
    global til2
    update.message.reply_text('Uzbekcha matn kiriting', reply_markup=back_btn)
    til1 = 'uz'
    til2 = 'ru'
    return 'TARJIMA'

def engrus(update,context):
    global til1
    global til2
    update.message.reply_text('Inglizcha matn kiriting', reply_markup=back_btn)
    til1 = 'en'
    til2 = 'ru'
    return 'TARJIMA'



def translate(update, context):
    matn = update.message.text    
    if matn==ORTGA:
        start(update, context)
        return 1
    else:    
        t_matn = tarjima(matn, til1, til2)
        update.message.reply_text(t_matn.text)    
        return 'TARJIMA'
    

def inline_callback(update, context):
    m = update.callback_query
    m.message.delete()
    m.message.reply_text(m.data)
    return 1

def main():
    updater = Updater(TOKEN, use_context=True)

    disp = updater.dispatcher

    conv_hand = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1:[
                CommandHandler('salom', salom)
            ],
            'call':[
                CallbackQueryHandler(inline_callback)
            ],
            2: [
                MessageHandler(Filters.regex('^(' + RUEN + ')$'), ruseng),  # ^(Ruscha-Inglizcha)$
                MessageHandler(Filters.regex('^(' + UZRU + ')$'), uzbru),
                MessageHandler(Filters.regex('^(' + ENRU + ')$'), engrus),
            ],
            'TARJIMA':[
                MessageHandler(Filters.text, translate)
            ],
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


# https://yandex.uz/pogoda/