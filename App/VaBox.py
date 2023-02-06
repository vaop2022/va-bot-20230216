#from VaActions import *
from VaDirectionDetector import getDirection



from  Action_000_module  import *
from  Action_010_module  import *
from  Action_020_module  import *
from  Action_030_module  import *
from  Action_040_module  import *
from  Action_9000_module  import *

def start(va_data,bot_data):
    
    Action_000(va_data,bot_data)

    bot_obj = bot_data.get('telebot.TeleBot(5662687046******)...b10')

    @bot_obj.message_handler(commands=['start'])
    def get_start(message):

        bot_data.set('message from customer...b11', message)
        bot_data.set('message type from customer...message type', bot_data.get('message_type constant: commands...commands'))

        action(va_data,bot_data)

    @bot_obj.message_handler()
    def get_user_text(message):
        bot_data.set('message from customer...b11', message)
        bot_data.set('message type from customer...message type', bot_data.get('message type constant: any_text...any text'))

        action(va_data,bot_data)

    @bot_obj.callback_query_handler(func = lambda call: True)
    def answer(call):
        bot_data.set('input [call.data] from customer...input from customer', call.data)
        bot_data.set('message type from customer...message type', bot_data.get('message_type constant: input...input'))

        action(va_data,bot_data)

    bot_obj.polling(non_stop=True)

def action(va_data,bot_data):

    getDirection(va_data,bot_data)
    va_script = va_data.get('VA script...va_script')
    current_action = va_data.get('The current Action...current action')
    direction = va_data.get('Direction...direction')

    temp = va_script[current_action][direction]
    
    va_data.set('The previous Action...previous action', current_action)
    va_data.set('The current Action...current action', temp)

    eval(va_data.get('The current Action...current action') + "(va_data,bot_data)")

