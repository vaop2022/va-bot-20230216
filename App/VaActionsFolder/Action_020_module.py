def Action_020(va_data,bot_data):
    print('Action_020')

    message = bot_data.get('message from customer...b11')
    bot_obj = bot_data.get('telebot_obj.TeleBot(5662687046******)...b10')

    mess = f'<b>Hi, I know about you )))</b>, {message}'
    bot_obj.send_message(message.chat.id, mess, parse_mode='html')
