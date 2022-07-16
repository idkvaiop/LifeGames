from typing import Text
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import telegram
import cowsay
import os
from gtts import gTTS
from googlesearch import search
from password_generator import PasswordGenerator
import requests
import json
from PyDictionary import PyDictionary
from random import random
import base64


TOKEN = os.getenv("BOT_TOKEN")
APP_NAME = os.getenv("APP_NAME")



def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\! welcome to @thezeroimagebot', )

def encode(update , context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    sample_string = update.message.reply_to_message.text
    sample_string_bytes = sample_string.encode("ascii")
  
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    update.message.reply_text(f"Encoded string: {base64_string}")

def decode(update , context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    base64_string = update.message.reply_to_message.text
    base64_bytes = base64_string.encode("ascii")
  
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    update.message.reply_text(f"Decoded string: {sample_string}")





    

def help_command(update , context):
    help_text='''
              *  /start to start the bot
              *  /source_code to retrive source code
              *  /donate to donate the creator
              *  /creator to know the creator
              *  /encode to encode an string in base64 format
              *  /decode to decode a string of base64 format
              *  /meaning to know meaning of word
              *  /search reply to a word to search in google
              *  /speak reply to a para/word to make it as audio file
              *  /cowsay input to make cowsay (mention text after command)
              *  /password to generate a strong password (mention len after command)
              *  /report to report a issue in bot
    
 
    
    
    
    '''
    update.message.reply_text(help_text)

def source_code(update, context):
    keyboard = [
        [
            telegram.InlineKeyboardButton("Source Code",
                                          url="https://github.com/raveen-2003/TheWordzBot"),
        ],
    ]

    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Source code of @theWordzBot is available in github", reply_markup=reply_markup)

def creator(update, context):
    update.message.reply_text('creator - @im_raveen')

def donate(update, context):
    keyboard = [
        [
            telegram.InlineKeyboardButton("Contribute",
                                          url="https://github.com/raveen-2003"),
            telegram.InlineKeyboardButton(
                "upi", url="https://upayi.me/raveen-2003@axl"),
        ],
    ]

    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Thank you for comming forward ! , your donations makes our bot Alive and encourages us to give more updates in near future", reply_markup=reply_markup)

def speak(update , context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text(reply_to_message_id=update.message.message_id, text= 'please wait ! processing', parse_mode='html')
    mytext = update.message.reply_to_message.text
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("./speak/@TheWordzBot.mp3")
    caption = "<b>text to speech by <a herf=\"http://t.me/thewordzbot\">@TheWordzBot</a></b>❤️"

    context.bot.send_document(chat_id=update.effective_chat.id, document=open('./speak/@TheWordzBot.mp3', 'rb'), caption=caption , parse_mode="html")

def moo(update , context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    text_got = context.args
    moo_say = str(text_got).split(":")[0].strip().replace("'", "").replace(",", "").replace("[",
                                                                                                                   "").replace(
        "]", "")
    update.message.reply_text(cowsay.get_output_string("cow", moo_say ))
    cowsay.cow(update.message.reply_to_message.text)
    cowsay_text = update.message.reply_to_message.text
    update.message.reply_text(cowsay.get_output_string("cow", cowsay_text ),parse_mode="markdown")


def pass_gen(update , context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    pwo = PasswordGenerator()
    number_got = context.args
    length = str(number_got).split(":")[0].strip().replace("'", "").replace(",", "").replace("[",
                                                                                                                   "").replace(
        "]", "")
    pwo.minlen = int(length) # (Optional)
    generator = pwo.generate()
    update.message.reply_text(generator)

def dictonary_f(update , context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
   
    update.message.reply_text(reply_to_message_id=update.message.message_id, text= 'please wait ! processing', parse_mode='html')
    Text_got =  context.args
    real_word = str(Text_got).split(":")[0].strip().replace("'", "").replace(",", "").replace("[",
                                                                                                                   "").replace(
        "]", "")
    dictionary=PyDictionary()
    update.message.reply_text((dictionary.meaning(real_word)))





def google(update , context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    update.message.reply_text(reply_to_message_id=update.message.message_id, text= 'please wait ! processing', parse_mode='html')
    
    search_txt_args = context.args
    txt_args_got = str(search_txt_args).split(":")[0].strip().replace("'", "").replace(",", "").replace("[",
                                                                                                                   "").replace(
        "]", "")
    r
    results = search(txt_args_got)
    update.message.reply_text(results)


def report(update, context):
    update.message.reply_text(''' Found a problem in bot ?
                              report it in @im_raveen
                              ''')



def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)
    PORT = int(os.environ.get('PORT', '8443'))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("speak", speak))
    dispatcher.add_handler(CommandHandler("cowsay", moo))
    dispatcher.add_handler(CommandHandler("search", google))
    dispatcher.add_handler(CommandHandler("password", pass_gen))
    dispatcher.add_handler(CommandHandler("meaning", dictonary_f))
    dispatcher.add_handler(CommandHandler("encode", encode))
    dispatcher.add_handler(CommandHandler("decode", decode))
    dispatcher.add_handler(CommandHandler("creator", creator))
    dispatcher.add_handler(CommandHandler("source_code", source_code))
    dispatcher.add_handler(CommandHandler("donate", donate))
    dispatcher.add_handler(CommandHandler("report", report))






    # on non command i.e message - echo the message on Telegram
    

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN,
                          webhook_url=f"https://{APP_NAME}.herokuapp.com/" + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()
