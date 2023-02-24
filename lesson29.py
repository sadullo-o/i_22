# py -m pip install opencv-python
import cv2
import urllib
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, filters
from urllib.request import urlopen
import numpy as np


def rasm2chizma(rasmurl):
    with urllib.request.urlopen(rasmurl) as r:
        img = np.asarray(bytearray(r.read()), dtype='uint8')

        img = cv2.imdecode(img, 0)
        cv2.imwrite('image.jpg', img)

    rasm = cv2.imread('image.jpg')
    gray_rasm = cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
    invert_rasm = cv2.bitwise_not(gray_rasm)

    blur_rasm = cv2.GaussianBlur(invert_rasm, (7,7), 0)

    invert_blur = cv2.bitwise_not(blur_rasm)

    chizma_rasm = cv2.divide(gray_rasm, invert_blur, scale=256.0)

    cv2.imwrite('rasm.jpg', chizma_rasm)



TOKEN = '6044418045:AAGsrn5tB8ZHLw2I8bhWl0uNzzVEhmQqRPo'


def start(update, context):
    update.message.reply_text('Rasm yuboring')
    return 1

def chizma(update, context):
    chat_id = update.message.chat_id
    rasm_id = update.message.photo[-1].file_id
    photo = context.bot.get_file(rasm_id)
    rasm2chizma(photo['file_path'])
    # update.message.reply_text(photo['file_path'])
    context.bot.send_document(chat_id, open('rasm.jpg', 'rb'))

def main():
    updater = Updater(TOKEN, use_context=True)
    disp = updater.dispatcher

    conv_hand = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1:[
                MessageHandler(filters.Filters.photo, chizma)
            ]
        },
        fallbacks=[CommandHandler('start', start)]
    )

    disp.add_handler(conv_hand)
    updater.start_polling()
    updater.idle()


main()

# tekshiramiz