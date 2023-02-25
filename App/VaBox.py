
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

#from VaActions import *
from VaDirectionDetector import getDirection
from TableClasses import Base, VaTraceTable
from VaData import VaData
import VaConfig

from  Action_000_module  import *
from  Action_010_module  import *
from  Action_020_module  import *
from  Action_030_module  import *
from  Action_040_module  import *
from  Action_9000_module  import *


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(va_data,bot_data):

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id

        va_data = VaData()
        VaConfig.setup(va_data)

        #bot_data.set('message from customer...b11', message)
        #bot_data.set('message type from customer...message type', bot_data.get('message_type constant: commands...commands'))

        action(va_data,bot_data, update, context)

        message_to_user = "/srart I'm a bot, please talk to me!"
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message_to_user)

    async def val(update: Update, context: ContextTypes.DEFAULT_TYPE):

        action(va_data,bot_data, update, context)

        message_to_user = "/val I'm a bot, please talk to me!"
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message_to_user)
    
    async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")



    application = ApplicationBuilder().token('6273699064:AAEw16IHpA_YEJ6a5nQdx-DkhpmojZzpYSQ').build()

    start_handler = CommandHandler('start', start)
    val_handler = CommandHandler('val', val)

    # Other handlers
    unknown_handler = MessageHandler(filters.COMMAND, unknown)


    application.add_handler(start_handler)
    application.add_handler(val_handler)

    application.add_handler(unknown_handler)

    application.run_polling()

def action(va_data, bot_data,  update, context):

    getDirection(va_data,bot_data,  update, context)
    va_script = va_data.get('VA script...va_script')
    current_action = va_data.get('The current Action...current action')
    direction = va_data.get('Direction...direction')

    temp = va_script[current_action][direction]
    
    va_data.set('The previous Action...previous action', current_action)
    va_data.set('The current Action...current action', temp)

    ### setContext
    #va_data.setContext(chat_id)     
    #print('Context variable dict...cvd', va_data.get('Context variable dict...cvd'))
    ###

    #trace(va_data,bot_data,chat_id)

    eval(va_data.get('The current Action...current action') + "(va_data,bot_data, update, context)")


"""
def start(va_data,bot_data):
    
    Action_000(va_data,bot_data)

    bot_obj = bot_data.get('telebot.TeleBot(5662687046******)...b10')

#### /start ##############################################################
    @bot_obj.message_handler(commands=['start'])
    def get_start(message):
        va_data = VaData()
        VaConfig.setup(va_data)

        bot_data.set('message from customer...b11', message)
        bot_data.set('message type from customer...message type', bot_data.get('message_type constant: commands...commands'))

        action(va_data,bot_data, message.chat.id)

#### any text  ##############################################################
    @bot_obj.message_handler()
    def get_user_text(message):

        va_data.getContext(message.chat.id)  

        bot_data.set('message from customer...b11', message)
        bot_data.set('message type from customer...message type', bot_data.get('message type constant: any_text...any text'))

        action(va_data,bot_data, message.chat.id)

#### from button  ##############################################################
    @bot_obj.callback_query_handler(func = lambda call: True)
    def answer(call):

        va_data.getContext(call.from_user.id)

        bot_data.set('input [call.data] from customer...input from customer', call.data)
        bot_data.set('message type from customer...message type', bot_data.get('message_type constant: input...input'))

        action(va_data,bot_data, call.from_user.id)

    bot_obj.polling(non_stop=True)

def action(va_data, bot_data, chat_id):

    getDirection(va_data,bot_data)
    va_script = va_data.get('VA script...va_script')
    current_action = va_data.get('The current Action...current action')
    direction = va_data.get('Direction...direction')

    temp = va_script[current_action][direction]
    
    va_data.set('The previous Action...previous action', current_action)
    va_data.set('The current Action...current action', temp)

    ### setContext
    va_data.setContext(chat_id)     
    print('Context variable dict...cvd', va_data.get('Context variable dict...cvd'))
    ###

    trace(va_data,bot_data,chat_id)

    eval(va_data.get('The current Action...current action') + "(va_data,bot_data)")

    

def trace(va_data,bot_data,chat_id_1):
    trace = VaTraceTable(
            chat_id = chat_id_1, 
            previous_action = va_data.get('The previous Action...previous action'), 
            direction = va_data.get('Direction...direction'), 
            current_action = va_data.get('The current Action...current action'),
            va_data_column = va_data.get('Context variable dict...cvd')
        ) 
        
    s = va_data.get('session...s')
    s.add(trace) 
    s.commit()


"""
