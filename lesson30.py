# from telegram.ext import Updater,CommandHandler,ConversationHandler,MessageHandler,Filters,filters
# from moviepy.editor import * 



# def mp44():
#     mp4 = r"video.mp4"
#     mp3 = r"audio.mp3"
#     video = VideoFileClip(mp4)
#     audio = video.audio
#     audio.write_audiofile(mp3)

#     audio.close()
#     video.close()



# TOKEN = '6193879079:AAHk2gv00Hx5nf9fA3XTglssN0napaFw_yM'

# def start(update, context):
#     update.message.reply_text('Video yuboring')
#     return 1

# def convert(update,context):
#     chat_id = update.message.chat_id
#     video_id= update.message.video.file_id
#     video = context.bot.get_file(video_id)
#     update.message.reply_text(video['file_path'])
#     #context.bot.send_document(chat_id, open('audio.mp3','rb'))





# def main():
#     updater = Updater(TOKEN, use_context=True)
#     disp = updater.dispatcher

#     conv_hand = ConversationHandler(
#         entry_points=[CommandHandler('start',start)],
#         states={
#             1:[
#                 MessageHandler(filters.Filters.video, convert)
#             ]
#         },
#         fallbacks=[CommandHandler('start',start)]
#     )
#     disp.add_handler(conv_hand)
#     updater.start_polling()
#     updater.idle()

# main()





# CTRL  SHIFT  P

# Test uchun



# Yana test