# from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
# and from https://youtu.be/StseQeseJbQ - CallbackQuery КОЛБЭКИ TELEGRAM БОТ -AIOGRAM (для чайников) - ПРОГРАММИРОВАНИЕ ПО ПЛЕЙЛИСТАМ УРОК 12


"""
How to write a bot telegram so that when you enter and execute the same command three times in a row, a message is displayed that you have already entered and executed this command three times in a row, for example, the command "/help"

from telegram.ext import Updater, CommandHandler

# Define a dictionary to keep track of command counts
command_counts = {}

# Define a function to handle the /help command
def help(update, context):
    # Get the user ID and command from the update
    user_id = update.effective_user.id
    command = "/help"

    # Get the current count for this user and command
    count = command_counts.get((user_id, command), 0)

    if count == 2:
        # If this is the third time the command has been executed in a row, send a warning message
        context.bot.send_message(chat_id=update.message.chat_id, text="You have already executed this command three times in a row!")
    else:
        # Otherwise, increment the count and execute the command as normal
        command_counts[(user_id, command)] = count + 1
        context.bot.send_message(chat_id=update.message.chat_id, text="This is the first or second time you have executed this command in a row.")

# Create an Updater object and register the command handler
updater = Updater(token='6273699064:AAEw16IHpA_YEJ6a5nQdx-DkhpmojZzpYSQ', use_context=True)
updater.dispatcher.add_handler(CommandHandler('help', help))

# Start the bot
updater.start_polling()

"""

import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

command_counts = {}
count = 0

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    command = "/help"
    command_counts[(user_id, command)] = 0
    await context.bot.send_message(chat_id=update.effective_chat.id, text="/srart I'm a bot, please talk to me!")

async def val(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the user ID and command from the update
    user_id = update.effective_user.id
    command = "/help"

    # Get the current count for this user and command
    count = command_counts.get((user_id, command), 0)

    if count == 2:
        # If this is the third time the command has been executed in a row, send a warning message
        await context.bot.send_message(chat_id=update.effective_chat.id, text="/val the third time the command has been executed!")
    else:
        # Otherwise, increment the count and execute the command as normal
        command_counts[(user_id, command)] = count + 1
        await context.bot.send_message(chat_id=update.effective_chat.id, text="/val I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")



if __name__ == '__main__':
    application = ApplicationBuilder().token('6273699064:AAEw16IHpA_YEJ6a5nQdx-DkhpmojZzpYSQ').build()
    
    start_handler = CommandHandler('start', start)
    val_handler = CommandHandler('val', val)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)
    inline_caps_handler = InlineQueryHandler(inline_caps)
    # Other handlers
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    

    application.add_handler(start_handler)
    application.add_handler(val_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(inline_caps_handler)

    application.add_handler(unknown_handler)
    
    application.run_polling()

