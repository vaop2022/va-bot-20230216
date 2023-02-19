from telebot import types
import random

def Action_030(va_data,bot_data):
    print('Action_030')

    debug_action = va_data.get('The current Action...current action')

    temp = {1:'Yes', 2:'No',3:'Up to You )'}

    rand = random.randint(1,2)
    
    mess = f'Answer is: {temp[rand]}'

    message = bot_data.get('message from customer...b11')
    bot_obj = bot_data.get('telebot_obj.TeleBot(5662687046******)...b10')
    
    markup_inline = types.InlineKeyboardMarkup()
    button_10 = types.InlineKeyboardButton(text = bot_data.get('button title...Again'), callback_data = bot_data.get('input from customer constant...again'))
    markup_inline.add(button_10)

    bot_obj.send_message(message.chat.id, debug_action+mess, reply_markup = markup_inline)
