from telebot import types

def Action_010(va_data,bot_data):
    print('Action_010')

    message = bot_data.get('message from customer...b11')
    bot_obj = bot_data.get('telebot_obj.TeleBot(5662687046******)...b10')

    markup_inline = types.InlineKeyboardMarkup()

    button_10 = types.InlineKeyboardButton(
            text = bot_data.get('button title...Yes/No'), 
            callback_data = bot_data.get('input from customer constant...yes or no')
        )

    button_20 = types.InlineKeyboardButton(
            text = bot_data.get('button title...Yes/No/Up to You'), 
            callback_data = bot_data.get('input from customer constant...yes or no or uptoyou')
        )

    markup_inline.add(button_10, button_20)

    mess = bot_data.get('Ask V-agent...msg_010')
    bot_obj.send_message(message.chat.id, mess, reply_markup = markup_inline)
