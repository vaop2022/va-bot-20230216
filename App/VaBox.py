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

